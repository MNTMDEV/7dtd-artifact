Name:           7dtd-server
Version:        1.0.0
Release:        1
Summary:        7 Days to Die Game Server
Summary(zh_CN): 七日杀服务端
Group:          System Environment/Daemons
License:        GPL
URL:            http://game.mntmdev.com/
Source0:        7dtd-server.tar.gz
BuildArch:      x86_64
BuildRoot:      %{_topdir}/BUILDROOT
Requires:       glibc(x86-32),libstdc++(x86-32)
%description
7 Days to Die Game Server (RPM Version)

%define debug_package %{nil}
%define _binpath /usr/bin
%define _servicepath /usr/lib/systemd/system
%define _steampath /usr/share/steamcmd

%prep
%setup -c -q

%build
wget https://steamcdn-a.akamaihd.net/client/installer/steamcmd_linux.tar.gz
mkdir steamcmd/
tar -zxvf steamcmd_linux.tar.gz -C steamcmd/

%install
rm -rf %{buildroot}/*
mkdir -p %{buildroot}%{_binpath}
mkdir -p %{buildroot}%{_servicepath}
mkdir -p %{buildroot}%{_steampath}

cp deploy/%{name}.service %{buildroot}%{_servicepath}
cp deploy/7dtd-server %{buildroot}%{_binpath}
cp deploy/steamcmd %{buildroot}%{_binpath}
chmod +x %{buildroot}%{_binpath}/7dtd-server
chmod +x %{buildroot}%{_binpath}/steamcmd
cp -r steamcmd/* %{buildroot}%{_steampath}

%clean
rm -rf %{buildroot}/*

%files
%{_binpath}/*
%{_servicepath}/*
%{_steampath}/*