%define ver  0.6.15
%define rel  1
%define jobs 2

Name:          nodejs
Version:       %{ver}
Release:       %{rel}
Summary:       Node's goal is to provide an easy way to build scalable network programs.
Group:         Applications/Internet
License:       Copyright Joyent, Inc. and other Node contributors.
URL:           http://nodejs.org
Source0:       http://nodejs.org/dist/node-v%{version}.tar.gz
BuildRoot:     %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)

BuildRequires: python >= 2.4

%description
Node.js is a server-side JavaScript environment that uses an asynchronous
event-driven model. This allows Node.js to get excellent performance based on
the architectures of many Internet applications.

%prep
%setup -q -n node-v%{version}

%build
export JOBS=%{jobs}
./configure --prefix=/usr
make

%install
rm -rf %{buildroot}
make install DESTDIR=%{buildroot}

%clean
rm -rf %{buildroot}

%files
%defattr(-,root,root,-)
%doc AUTHORS ChangeLog LICENSE README.cmake README.md TODO TODO.win32

     /usr/bin/node
     /usr/bin/node-waf
     /usr/include/node
     /usr/lib/node
     /usr/lib/pkgconfig/nodejs.pc
     /usr/share/man/man1/node.1.gz

%changelog
* Thu Apr 12 2012 Vibol Hou <vibol@hou.cc> 0.6.15-1
- Initial rpm using upstream v0.6.15

* Thu Apr 14 2011 Chris Abernethy <cabernet@chrisabernethy.com> 0.4.6-1
- Initial rpm using upstream v0.4.6
