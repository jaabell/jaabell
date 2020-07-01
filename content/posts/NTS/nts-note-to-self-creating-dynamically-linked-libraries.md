Title: NTS (Note-To-Self): Creating dynamically linked libraries
date: 2013-10-28 18:57
Author: jaabell
Tags: c++, coding, compiler, gcc, library, linux, note to self, programming, reminder, tutorial
Slug: nts-note-to-self-creating-dynamically-linked-libraries

A nice extensive tutorial can be found [here](<http://www.yolinux.com/TUTORIALS/LibraryArchives-StaticAndDynamic.html>).

In a nutshell:

    :::shell.BashLexer
    gcc -Wall -fPIC -c \*.c  
    gcc -shared -Wl,-soname,libctest.so.1 -o libctest.so.1.0 \*.o  
    mv libctest.so.1.0 /opt/lib  
    ln -sf /opt/lib/libctest.so.1.0 /opt/lib/libctest.so.1  
    ln -sf /opt/lib/libctest.so.1.0 /opt/lib/libctest.so  


<!--more-->

-   `-Wall`: include warnings. See man page for warnings specified.
-   `-fPIC`: Compiler directive to output position independent code, a
    characteristic required by shared libraries. Also see
    "-fpic".
-   `-shared`: Produce a shared object which can then be linked with other objects
    to form an executable.
-   `-Wl,options`: Pass options to linker.
-   In this example the options to be passed on to the linker are: `-soname
    libctest.so.1`. The name after the `-o` option is passed to
    gcc.
-   Option `-o`:
    Output of operation. In this case the name of the shared object to
    be output will be `libctest.so.1.0`

See note on "Library Paths"
