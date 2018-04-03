Title: Como compilar kratos en leftraru 
Slug: como-compilar-kratos-en-leftraru
Date: Wed 28 Mar 2018 03:43:59 PM -03
Tags: 
Category: 
Author: jaabell
Lang: 
Summary: 
status: hidden

# Como compilar kratos en leftraru 

Resumen: *hay que compilar todo a mano*



##Cargar modulos necesarios:

    module load intel/2018c       
    module load impi/2018.2.199   
    module load metis/5.1.0

##Descargar dependencias: 

Necesitamos descargar y compilar a mano las siguientes librerias

* zlib
* Python3
* Trilinos
* Boost
* Kratos

Bajarlas usando:

    wget https://zlib.net/zlib-1.2.11.tar.gz
    wget https://www.python.org/ftp/python/3.5.5/Python-3.5.5.tgz
    wget http://trilinos.csbsju.edu/download/files/trilinos-12.12.1-Source.tar.gz
    wget https://sourceforge.net/projects/boost/files/boost/1.59.0/boost_1_59_0.tar.gz
    git clone https://github.com/KratosMultiphysics/Kratos.git

Descomprimir dependencias:

    tar -xzvf zlib-1.2.11.tar.gz
    tar -xzvf Python-3.5.5.tgz
    tar -xzvf trilinos-12.12.1-Source.tar.gz
    tar -xzvf boost_1_59_0.tar.gz

## Compilar zlib

    cd zlib-1.2.11
    export CC=icc
    export CFLAGS='-O3 -xHost -ip'
    ./configure --prefix=$HOME
    make -j 20
    make install

Una vez listo, deberiamos tener las librerias compiladas en `$HOME`.

    ls $HOME/lib/libz*

Entrega algo como:

    /home/jabell/lib/libz.a  /home/jabell/lib/libz.so  /home/jabell/lib/libz.so.1  /home/jabell/lib/libz.so.1.2.11

Volver al home 

    cd ~

## Compilar python3

Compilar e instalar

    cd Python-3.5.5
    ./configure --with-icc --without-gcc --prefix=$HOME --enable-shared
    make -j 20
    make install

Hacer un link simbolico para que no se maree trilinos

    cd ~/include
    ln -s python3.5m/ python3.5
    cd ..


## Compilar boost

Esto es cacho. Tener paciencia, como dice el compilador a cada rato...

    cd boost_1_59_0
    ./bootstrap.sh  --with-python-version=3.5 --with-libraries=python,mpi,serialization --with-toolset=intel-linux --with-python=$HOME/bin/python3.5m --with-python-root=$HOME/

Editar `project-config.jam` usando nano

    nano project-config.jam

Al final del archivo agregar la linea:

    using mpi : /home/apps/intel/2018/compilers_and_libraries_2018.2.199/linux/mpi_2019/intel64/bin/mpicc ;

Luego llamar el compilado:

    ./b2 stage --with-python --with-serialization --with-mpi variant=release cxxflags="-std=c++11" link=shared address-model=64 toolset=intel 
    ./b2 install --prefix=$HOME
    cd ..


## Compilar Trilinos

En este se usa CMAKE

    cd trilinos-12.12.1-Source
    mkdir build

Crear `do_configure.sh` estos eran los contenidos del mio:

    TRILINOS_ROOT="${HOME}/trilinos-12.12.1-Source"
    EXTRA_LINK_FLAGS=""
    EXTRA_ARGS=$@
    MPI_ROOT="${MPI_ROOT}"
    METIS_ROOT="/home/apps/parmetis/4.0.3/"
    LAPACK_ROOT="${MKLROOT}/lib/intel64"

    echo "TRILINOS_ROOT = $TRILINOS_ROOT"
    echo "EXTRA_LINK_FLAGS = $EXTRA_LINK_FLAGS"
    echo "EXTRA_ARGS = $EXTRA_ARGS"
    echo "MPI_ROOT = $MPI_ROOT"
    echo "METIS_ROOT = $METIS_ROOT"
    echo "LAPACK_ROOT = $LAPACK_ROOT"

    rm CMakeCache.txt
    rm -rf CMakeFiles
    rm *.cmake


    module load intel/2018c       
    module load boost/1.59        
    module load python/3.5.2      
    module load parmetis/4.0.3
    module load impi/2018.2.199   
    module load llvm/3.8.1        
    module load metis/5.1.0


    cmake \
      -DCMAKE_INSTALL_PREFIX:FILEPATH="${TRILINOS_ROOT}" \
      -DCMAKE_BUILD_TYPE:STRING=RELEASE \
      -DTrilinos_SOURCE_DIR="${TRILINOS_SOURCE}" \
      -DCMAKE_CXX_COMPILER=icpc \
      -DCMAKE_C_COMPILER=icc \
      -DCMAKE_Fortran_COMPILER=ifort \
      -DTPL_ENABLE_MPI:BOOL=ON \
      -DTrilinos_ENABLE_CXX11=ON\
      -DMPI_BASE_DIR="${MPI_ROOT}" \
      -DMPI_INCLUDE_DIRS:PATH="${MPI_ROOT}/include" \
      -DBUILD_SHARED_LIBS:BOOL=ON \
      -DBLAS_LIBRARY_DIRS:FILEPATH="${MKLROOT}/lib/intel64" \
      -DBLAS_LIBRARY_NAMES:STRING="mkl_rt" \
      -DLAPACK_LIBRARY_DIRS:FILEPATH="${MKLROOT}/lib/intel64" \
      -DLAPACK_LIBRARY_NAMES:STRING="mkl_rt" \
      -DTPL_ENABLE_MKL:BOOL=ON \
      -DMKL_LIBRARY_DIRS:FILEPATH="${MKLROOT}/lib/intel64" \
      -DMKL_LIBRARY_NAMES:STRING="mkl_rt" \
      -DMKL_INCLUDE_DIRS:FILEPATH="${MKLROOT}/include" \
      -DTPL_ENABLE_ParMETIS:BOOL=ON \
      -DParMETIS_INCLUDE_DIRS:PATH="${METIS_ROOT}/include" \
      -DParMETIS_LIBRARY_NAMES:STRING="parmetis" \
      -DParMETIS_LIBRARY_DIRS:PATH="${METIS_ROOT}/lib" \
      -DTPL_ENABLE_METIS:BOOL=ON \
      -DMETIS_INCLUDE_DIRS:PATH="${METIS_ROOT}/include" \
      -DMETIS_LIBRARY_NAMES:STRING="metis" \
      -DMETIS_LIBRARY_DIRS:PATH="${METIS_ROOT}/lib" \
      -DTrilinos_EXTRA_LINK_FLAGS:STRING="$EXTRA_LINK_FLAGS" \
      -DTrilinos_ENABLE_Amesos:BOOL=ON \
      -DAmesos_ENABLE_SuperLUDist:BOOL=OFF \
      -DTrilinos_ENABLE_Anasazi:BOOL=ON \
      -DTrilinos_ENABLE_AztecOO:BOOL=ON \
      -DAztecOO_ENABLE_Teuchos:BOOL=ON \
      -DTrilinos_ENABLE_Didasko:BOOL=ON \
      -DTrilinos_ENABLE_Epetra:BOOL=ON \
      -DTrilinos_ENABLE_EpetraExt:BOOL=ON \
      -DTrilinos_ENABLE_Galeri:BOOL=ON \
      -DTrilinos_ENABLE_Ifpack:BOOL=ON \
      -DTrilinos_ENABLE_ML:BOOL=ON \
      -DTrilinos_ENABLE_PyTrilinos:BOOL=OFF \
      -DTrilinos_ENABLE_Teuchos:BOOL=ON \
      -DTrilinos_ENABLE_Triutils:BOOL=ON \
      -DDART_TESTING_TIMEOUT:STRING=600 \
      -DCMAKE_Fortran_FLAGS:STRING="-O5 -funroll-all-loops -fPIC" \
      -DCMAKE_C_FLAGS:STRING="-O3 -fPIC -funroll-loops -march=native" \
      -DCMAKE_CXX_FLAGS:STRING="-O3 -fPIC -funroll-loops -ffast-math -march=native -DMPICH_IGNORE_CXX_SEEK" \
      $EXTRA_ARGS \
      ${TRILINOS_SOURCE} ..


Preparar compilado

    sh do_configure.sh
    make -j 20

TENER MUCHA PACIENCIA

    cd ..


## Compilar Kratos

    cd Kratos

Descargar `tetgen`

    cd applications/PfemApplication/external_modules/
    git clone https://github.com/ufz/tetgen.git
    cd ../../../    

Preparar configuracion

    mkdir build
    cd build
    nano conf.sh

Este es mi archivo `conf.sh`.

    #!/bin/sh

    # this is an example file...please DO NOT MODIFY if you don't want to do it for everyone
    #to use it, copy it to another file and run it

    # additional compiler flags could be added customizing the corresponding var, for example
    # -DCMAKE_CXX_FLAGS="${CMAKE_CXX_FLAGS} -msse3 ". Note that the "defaults are already correctly coded"
    #so we should ass here only machine specific stuff

    #an effort is made to autodetect all of the libraries needed HOWEVER:
    #METIS_APPLICATION needs the var PARMETIS_ROOT_DIR to be specified by the user (not needed if the app is set to OFF)
    #TRILINOS_APPLICATION needs the var PARMETIS_ROOT_DIR to be specified by the user (not needed if the app is set to OFF)
    #MKL_SOLVERS_APPLICATION needs the var MKLSOLVER_INCLUDE_DIR and MKLSOLVER_LIB_DIR to be specified by the user (not needed if the app is set to OFF)
    #note that the MKLSOLVER_LIB_DIR should include /lib/em64t. This is needed as intel is changing location of mkl at every update of the compiler!!

    #the user should also note that the symbol "\" marks that the command continues on the next line. IT SHOULD ONLY BE FOLLOWED
    #BY the "ENTER" and NOT by any space!!

    clear

    module load intel/2018c            
    module load impi/2018.2.199   
    module load metis/5.1.0

    #you may want to decomment this the first time you compile
    rm CMakeCache.txt
    rm *.cmake
    rm -rf CMakeFiles\

    cmake ..                                                              \
        -DCMAKE_C_COMPILER=icc                                                \
        -DCMAKE_INSTALL_RPATH_USE_LINK_PATH=TRUE                              \
        -DCMAKE_INSTALL_RPATH="$HOME/Kratos/libs"                      \
        -DCMAKE_CXX_COMPILER=icpc                                             \
        -DCMAKE_CXX_FLAGS="${CMAKE_CXX_FLAGS} -msse3 -std=c++11 "             \
        -DCMAKE_C_FLAGS="${CMAKE_C_FLAGS} -msse3 "                            \
        -DBOOST_ROOT="$HOME/"                             \
        -DPYTHON_LIBRARY="$HOME/lib/libpython3.5m.so"        \
        -DPYTHON_INCLUDE_DIR="$HOME/include/python3.5m"                \
        -DCMAKE_BUILD_TYPE=Release                                            \
        -DCONSTITUTIVE_MODELS_APPLICATION=ON                                  \
        -DFLUID_DYNAMICS_APPLICATION=ON                                       \
        -DCONVECTION_DIFFUSION_APPLICATION=ON                                 \
        -DDEM_APPLICATION=ON                                                  \
        -DSWIMMING_DEM_APPLICATION=OFF                                        \
        -DINCOMPRESSIBLE_FLUID_APPLICATION=ON                                 \
        -DMESHING_APPLICATION=ON                                              \
        -DEXTERNAL_SOLVERS_APPLICATION=ON                                     \
        -DSTRUCTURAL_APPLICATION=ON                                           \
        -DSTRUCTURAL_MECHANICS_APPLICATION=ON                                 \
        -DALE_APPLICATION=ON                                                  \
        -DFSI_APPLICATION=ON                                                  \
        -DMAPPING_APPLICATION=OFF                                             \
        -DOPENCL_APPLICATION=OFF                                              \
        -DMIXED_ELEMENT_APPLICATION=ON                                        \
        -DINSTALL_EMBEDDED_PYTHON=ON                                          \
        -DSHAPE_OPTIMIZATION_APPLICATION=ON                                   \
        -DTOPOLOGY_OPTIMIZATION_APPLICATION=OFF                               \
        -DPFEM_APPLICATION=ON                                                 \
        -DPFEM_FLUID_DYNAMICS_APPLICATION=ON                                  \
        -DCONTACT_MECHANICS_APPLICATION=ON                                    \
        -DSOLID_MECHANICS_APPLICATION=ON                                      \
        -DPFEM_SOLID_MECHANICS_APPLICATION=ON                                 \
        -DPARTICLE_MECHANICS_APPLICATION=ON                                   \
        -DUMAT_APPLICATION=ON                                                 \
        -DMETIS_APPLICATION=ON                                                \
        -DMETIS_INCLUDE_DIR="/home/apps/metis/5.1.0/include"               \
        -DMETIS_ROOT_DIR="/home/apps/metis/5.1.0/"               \
        -DUSE_METIS_5=ON                                                      \
        -DTRILINOS_APPLICATION=ON                                             \
        -DTRILINOS_LIBRARY_DIR="$HOME/trilinos-12.12.1-Source/lib"     \
        -DTRILINOS_INCLUDE_DIR="$HOME/trilinos-12.12.1-Source/include" \
        -DCONVECTION_DIFFUSION_APPLICATION=ON                                 \
        -DEXTERNAL_SOLVERS_APPLICATION=ON                                     \
        -DSOLID_MECHANICS_APPLICATION=ON                                      \
        -DZLIB_LIBRARY="$HOME/lib/libz.so"                                      \
        -DPOROMECHANICS_APPLICATION=ON                                        

Luego configurar, compilar e instalar

    sh conf.sh
    make -j 20
    make install

Irse a caminar un rato o practicar los trucos de magia...

Al instalar, si sale un error parecido a:

    CMake Error at cmake_install.cmake:69 (FILE):
       file INSTALL cannot find "/home/jabell/Kratos/-lm".


Editar `cmake_install.sh`

    nano cmake_install.sh

Y quitar (CTRL+K) la linea que dice:

    "/home/jabell/Kratos/-lm"

(Pro tip: busqueda con nano es "CTRL+/" colocar `-lm`).
    
## Modificar .bashrc

Editar `.bashrc`

    cd ~
    nano .bashrc

Agregar las siguientes lineas al final del `.bashrc`
    
    export PATH=$PATH:/home/jabell/Kratos/
    export PYTHONPATH=$PYTHONPATH:/home/jabell/Kratos/
    export LD_LIBRARY_PATH=$LD_LIBRARY_PATH:/home/jabell/Kratos/libs
    export LD_LIBRARY_PATH=$LD_LIBRARY_PATH:/home/jabell/lib


    module load parmetis/4.0.3
    module load metis/5.1.0

Guardar y salirse. Incorporar los cambios al `.bashrc`

    source .bashrc

## PROBAR LA BESTIA!!!

Crear un archivo `testkratos.py` en el home

    nano testkratos.py 

Poner adentro:

    from KratosMultiphysics import *
    from KratosMultiphysics.mpi import *
    from KratosMultiphysics.MetisApplication import *
    from KratosMultiphysics.TrilinosApplication import *

Guardar y ejecutar

    runkratos testkratos.py

Deberia resultar en 

     |  /           |             
     ' /   __| _` | __|  _ \   __|
     . \  |   (   | |   (   |\__ \ 
    _|\_\_|  \__,_|\__|\___/ ____/
               Multi-Physics 6.0.0-4212599
    Importing    KratosMetisApplication
    Initializing Kratos MetisApplication... 
    Importing    KratosTrilinosApplication
         KRATOS   _____     _ _ _                 
                 |_   _| __(_) (_)_ __   ___  ___ 
                   | || '__| | | | '_ \ / _ \/ __|
                   | || |  | | | | | | | (_) \__ \
                   |_||_|  |_|_|_|_| |_|\___/|___/ APPLICATION     
    KRATOS TERMINATED CORRECTLY


## Probar Kratos en el gestor de colas

Crear un batch script para SLURM (el gestor de colas) llamado `testkratos.sh` que contenga

    #!/bin/bash -l
    #SBATCH -n 2  # pedir dos procesos
    #SBATCH -J testkratos
    #SBATCH --time=00:01:00  #Time requested
    #SBATCH --error=testkratos.%A.err
    #SBATCH --output=testkratos.%A.out
    #SBATCH --mail-type=ALL # Type of email notification- BEGIN,END,FAIL,ALL
    #SBATCH --mail-user=ja.abell@gmail.com # Email to which notifications will be sent

    srun runkratos testkratos.py

Este archivo especifica los requerimientos de recursos a leftraru. Debiera ser bastante obvio lo que significa todo. Por siacaso aqui esta la expliacion

Pedir cantidad de procesos

    #SBATCH -n 2  # pedir dos procesos

Hay comandos para solicitar cierto numero de nodos o de proceso por nodo y otras configuraciones. Tambien se pueden correr `arreglos` o familias de tareas relacionadas usando la opcion `array`.

Nombre de la tarea 

    #SBATCH -J testkratos

Tiempo solicitado.

    #SBATCH --time=00:01:00  #Time requested

La salida del programa, error y standar-out, se redirigen a los archivos especificados por las lineas:

    #SBATCH --error=testkratos.%A.err
    #SBATCH --output=testkratos.%A.out

Donde `%A` se reemplaza por el numero de la tarea. 

Para mandar un email con cada cambio de estado de la tarea usar:

    #SBATCH --mail-type=ALL # Type of email notification- BEGIN,END,FAIL,ALL
    #SBATCH --mail-user=ja.abell@gmail.com # Email to which notifications will be sent

Finalmente, este es el comando que queremos ejecutar:

    srun runkratos testkratos.py

Pueden haber mas comandos o pasos a seguir. Aqui `srun` reemplaza la llamada a `mpirun`.

Ejecutar el script (poner en la cola)

    sbatch testkratos.sh

Deberia decir algo como 

    Submitted batch job 10894854

Se puede revisar el status de la tarea solicitada mediante

    squeue
    
Que dice algo como esto cuanto la tarea esta corriendo 

    [jabell@leftraru3 ~]$ squeue
                 JOBID PARTITION     NAME     USER ST       TIME  NODES NODELIST(REASON)
              10894854     slims testkrat   jabell PD       0:00      1 (Priority)

La salida del programa la encontramos en los archivos .err y .out generados. En mi caso, 

    more testkratos.10894854.4294967294.err

Resulta vacio, y 

    more testkratos.10894854.4294967294.out

resulta en 

     |  /           |             
     ' /   __| _` | __|  _ \   __|
     . \  |   (   | |   (   |\__ \ 
    _|\_\_|  \__,_|\__|\___/ ____/
               Multi-Physics 6.0.0-4212599
     |  /           |             
     ' /   __| _` | __|  _ \   __|
     . \  |   (   | |   (   |\__ \ 
    _|\_\_|  \__,_|\__|\___/ ____/
               Multi-Physics 6.0.0-4212599
    Initializing Kratos MetisApplication... 
    Initializing Kratos MetisApplication... 
         KRATOS   _____     _ _ _                 
                 |_   _| __(_) (_)_ __   ___  ___ 
                   | || '__| | | | '_ \ / _ \/ __|
                   | || |  | | | | | | | (_) \__ \
                   |_||_|  |_|_|_|_| |_|\___/|___/ APPLICATION     
    Importing    KratosMetisApplication
    Importing    KratosTrilinosApplication
    KRATOS TERMINATED CORRECTLY
    Importing    KratosMetisApplication
    Importing    KratosTrilinosApplication
    KRATOS TERMINATED CORRECTLY

Notar que corrieron dos Kratos (pedimos dos procesos). Supongo que hay mas cambios que hay que hacer en los scripts python que queremos correr, pero eso es todo por ahora. 


![Arrivederci](https://i.gifer.com/4xw2.gif)

