#!/usr/bin/tclsh

set arch "noarch"
set base "pgintcl-3.5.1"
set fileurl "https://sourceforge.net/projects/pgintcl/files/3.5.1/pgintcl-3.5.1.tgz"

set var [list wget $fileurl -O $base.tgz]
exec >@stdout 2>@stderr {*}$var

if {[file exists build]} {
    file delete -force build
}

file mkdir build/BUILD build/RPMS build/SOURCES build/SPECS build/SRPMS
file copy -force $base.tgz build/SOURCES

set buildit [list rpmbuild --target $arch --define "_topdir [pwd]/build" -bb pgintcl.spec]
exec >@stdout 2>@stderr {*}$buildit

# Remove our source code
file delete -force $base.tgz

