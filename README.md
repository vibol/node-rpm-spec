node rpm specfile
=================
Node.js does not come with RPMs for CentOS 6.3. Here are instructions to build node rpms from source.

Steps to build
--------------------------------------------------------
1. sudo yum groupinstall 'Development Tools'
2. sudo yum install openssl-devel python
3. mkdir -p ~/rpmbuild/BUILD ~/rpmbuild/RPMS ~/rpmbuild/RPMS/i386 ~/rpmbuild/RPMS/noarch ~/rpmbuild/RPMS/x86_64 ~/rpmbuild/RPMS/ ~/rpmbuild/SOURCES ~/rpmbuild/SPECS ~/rpmbuild/SRPMS
4. echo '%_topdir %(echo $HOME)/rpmbuild' >> ~/.rpmmacros
5. wget -P ~/rpmbuild/SOURCES http://nodejs.org/dist/v0.8.18/node-v0.8.18.tar.gz
6. wget -P ~/rpmbuild/SPECS https://raw.github.com/vibol/node-rpm-spec/master/nodejs.spec
7. rpmbuild -ba ~/rpmbuild/SPECS/nodejs.spec
8. rm ~/.rpmmacros
