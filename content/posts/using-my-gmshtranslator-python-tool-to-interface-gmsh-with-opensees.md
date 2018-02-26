Title: Using my gmshtranslator python tool to interface gmsh with opensees.
Slug: using-my-gmshtranslator-python-tool-to-interface-gmsh-with-opensees
Date: 2018-02-26 13:55:13
Modified: 2018-02-26 13:55:13
Tags: opensees, gmsh, gmshtranslator, python, pre-proceesing, meshing
Author: jaabell

I wrote the [*gmshtranslator*](https://github.com/jaabell/gmshtranslator) tool a while back during my PhD, to easily parse [*gmsh*](http://gmsh.info/) `msh` files to any other format. I've been using it for years now with not much change for both research and consulting, and have been contacted by other researchers that want to use it. I will soon write a tool, powered by *gmshtranslator*, to more easily translate from *gmsh* into OpenSees. Meanwhile, here is a short example on how to use gmshtranslator to create [*OpenSees*](opensees.berkeley.edu) models. The example assumes you know *gmsh* formats (`.geo` and `.msh`) and python. 

The example consists on the simple cantilever beam shown in the following figure.

![Beam](https://www.dropbox.com/s/96dqfc5r6su4pjd/beam.png?raw=1)


The beam is fixed at the right end, and has node-by-node forcing on the right end. The following *gmsh* `.geo.` script prepares the domain. 

**`beam.geo : `**

    LX = 5; LY = 0.5; Nx = 40; Ny = 5;

    Point(1) = {0, 0, 0, 1};
    Point(2) = {LX, 0, 0, 1};
    Point(3) = {LX, LY, 0, 1};
    Point(4) = {0, LY, 0, 1};
    Line(1) = {1, 2};
    Line(2) = {2, 3};
    Line(3) = {3, 4};
    Line(4) = {4, 1};
    Line Loop(1) = {1, 2, 3, 4};
    Plane Surface(1) = {1};

    Transfinite Line {1,3} = Nx+1;
    Transfinite Line {2,4} = Ny+1;
    Transfinite Surface{1};
    Recombine Surface{1};

    Physical Line("Fixed") = {4};
    Physical Line("Forcing") = {2};
    Physical Surface("Beam") = {1};

    Mesh(2);

3 physical groups are defined: *fixed* to identify the fixed nodes, *forcing* to identify the nodes that will carry loads, and *beam* contains all the quad elements to represent the body of the beam. Note the optional use of the transfinite meshing algorithm. Once this script is executed in *gmsh* the `.msh` file can be exported. The resulting `.msh` file can be found [here](https://www.dropbox.com/s/3d44h0ttdrm67gz/beam.msh?dl=0). 

*gmshtranslator* parses the `.msh` file, executing code depending on certain user-defined rules. What we want to do is define an opensees node command for each node in the `.msh` file, fix the nodes contained in the *fixed* physical group, generate forces for the nodes in the *forcing* physical group, and add quad elements for each quad in the `.msh` file. 

First, import the `beam.msh` file into *gmshtranslator* and open files to be written that will contain the opensees code. 

    from gmshtranslator import gmshTranslator

    mshfname = "beam.msh"

    gt = gmshTranslator(mshfname)

    fid_nodes =    open(mshfname.replace(".msh", ".nodes.tcl"),"w")
    fid_elements = open(mshfname.replace(".msh", ".elements.tcl"),"w")
    fid_fixities = open(mshfname.replace(".msh", ".fixities.tcl"),"w")
    fid_loads = open(mshfname.replace(".msh", ".loads.tcl"),"w")

I like writing different things (nodes, elements, etc.) in separate files for debugging. Your style might be different. *gmshtranslator* parses the file and evaluates *rules*. A rule is composed of a *condition* that must be met and an *action* to be executed, these are both python functions. There are rules for nodes and for elements. 

The syntax for node and element conditions are:

    def node_condition(tag,x,y,z,physgroups): 
    def element_condition(eletag,eletype,physgrp,nodes):

These are functions that evaluate to `true` or `false` depending on the inputs. Then the syntax for *actions* are:

    def node_action(tag,x,y,z):
    def element_action(eletag,eletype,physgrp,nodes):

These functions don't return anything, instead excecute whatever code should be executed if the *condition* of the rule is met. Rules are added to the parser by using the `add_nodes_rule` or `add_elements_rule` function of *gmshtranslator* and are excecuted whenever the `parse()` method is called. 

For example, the rule to add all nodes to the opensees domain would be:

    def is_node(tag,x,y,z,physgroups):
        return True

    def add_node(tag,x,y,z):
        fid_nodes.write("node {} {} {}\n".format(tag, x, y))

    gt.add_nodes_rule(is_node, add_node)

The node *condition* (`is_node`) function always returns `true`, that is this rule will execute for all nodes. The *action* function is `add_node` and will write the appropriate text into the nodes file. The *rule* is added into the parser by using the `gt.add_nodes_rule` function which accepts two python functions as arguments: a condition and an action. 

The code for the rest of the example is:

    def fix_node(tag,x,y,z):
        fid_fixities.write("fix {} 1 1\n".format(tag))

    def add_load(eletag,eletype,physgrp,nodes):
        fid_loads.write("load {} $fx $fy\n".format(nodes[0]))
        fid_loads.write("load {} $fx $fy\n".format(nodes[1]))

    def add_element(eletag,eletype,physgrp,nodes):
        fid_elements.write("element quad {} {} {} {} {} $thick PlaneStress $mat_tag\n".format(eletag, nodes[0], nodes[1], nodes[2], nodes[3]))
        

    gt.add_nodes_rule(gt.is_node_in("Fixed"), fix_node)

    gt.add_elements_rule(gt.is_element_in("Forcing"), add_load)
    gt.add_elements_rule(gt.is_element_in("Beam"), add_element)

Note that we didn't write a condition for the `fix_node` action, instead we used some of the simple conditions contained in *gmshtranslator* that can simplify some typical situations. In this case the `gt.is_node_in()` function takes a physical group name and evaluates whether each node is in that physical group. An equivalent `python` code for this would be:

    Fixed = 1  # Physical group number assigned by gmsh to the 'Fixed' group
    def is_node_in_Fixed(tag, x, y, z, physgroups):
        return Fixed in physgroups

Or using *gmstranslator*s internal mapping.

    def is_node_in_Fixed(tag, x, y, z, physgroups):
        return gt.physical_groups_by_name['Fixed'] in physgroups\

The same holds true for the `add_load` and `add_element` rules, I just opted to use the simple function but could have written a condition function from scratch.  Add all rules to the parser by callig the `add_X_rule` functions. Finally, call parse to execute and generate all output files. 

    gt.parse()

Don't forget to close files people!

    fid_nodes.close()
    fid_elements.close()
    fid_fixities.close()
    fid_loads.close()

Run the python script and, voillá! Meshing done. 

Finally, for completeness, here is the OpenSees tcl code that runs the complete example. I used elastic-isotropic material and a simple static analysis. I added only vertical loading on the tip of the beam. 


    model BasicBuilder -ndm 2 -ndf 2

    set thick 1.0

    set mat_tag 1
    set E 200.e9
    set nu 0.3

    nDMaterial ElasticIsotropic $mat_tag $E $nu

    source "beam.nodes.tcl"
    source "beam.fixities.tcl"
    source "beam.elements.tcl"

    set tstag 1
    timeSeries Linear $tstag 1.0

    set Ly 0.5
    set Ny 5
    set dy [expr $Ly/$Ny]

    set fx [expr 0*$dy/2]
    set fy [expr -10.*$dy/2]

    pattern Plain 1 "Linear" {
        source "beam.loads.tcl"
    }

    recorder pvd disp disp

    constraints Plain
    numberer RCM
    system UmfPack
    test NormDispIncr 1.0e-9 10
    algorithm Newton
    integrator LoadControl 1
    analysis Static
    analyze 1

The `pvd` recorder is used to generate a nice output file that can be viewed using [paraview](https://www.paraview.org/). 

![Deflections](https://www.dropbox.com/s/24tkmfk1y1r0wz5/disp.png?raw=1)