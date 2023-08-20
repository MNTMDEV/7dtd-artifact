#! /bin/bash
yum install glibc.i686 libstdc++.i686 -y
[ -d script/output/rpmbuild/SOURCES ] || mkdir -p script/output/rpmbuild/SOURCES
tar -zcvf script/output/rpmbuild/SOURCES/7dtd-server.tar.gz ./deploy
PROJECT_ROOT=`pwd`
RPM_ROOT=$PROJECT_ROOT/script/output/rpmbuild
rpmbuild -bb $PROJECT_ROOT/script/server.spec --define="_topdir $RPM_ROOT"