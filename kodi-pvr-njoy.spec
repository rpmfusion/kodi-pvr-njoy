%global commit 67b837d2daecce340342084b20a7a2c94b0ccc93
%global shortcommit %(c=%{commit}; echo ${c:0:7})
%global commitdate 20171228

%global kodi_addon pvr.njoy
%global kodi_version 18.0

Name:           kodi-%(tr "." "-" <<<%{kodi_addon})
# Use Epoch to manage upgrades from older upstream
# (https://github.com/opdenkamp/xbmc-pvr-addons/)
Epoch:          1
Version:        3.3.0
Release:        1%{?dist}
Summary:        NJOY PVR for Kodi

License:        GPLv2+
URL:            https://github.com/kodi-pvr/%{kodi_addon}/
Source0:        https://github.com/kodi-pvr/%{kodi_addon}/archive/%{shortcommit}/%{kodi_addon}-%{shortcommit}.tar.gz

BuildRequires:  cmake
BuildRequires:  gcc-c++
BuildRequires:  kodi-devel >= %{kodi_version}
BuildRequires:  kodi-platform-devel >= %{kodi_version}
BuildRequires:  pkgconfig(tinyxml)
BuildRequires:  platform-devel
Requires:       kodi >= %{kodi_version}
ExclusiveArch:  i686 x86_64

%description
%{summary}.


%prep
%autosetup -n %{kodi_addon}-%{commit}


%build
%cmake .
%make_build


%install
%make_install


%files
%doc README.md %{kodi_addon}/changelog.txt
%{_libdir}/kodi/addons/%{kodi_addon}/
%{_datadir}/kodi/addons/%{kodi_addon}/


%changelog
* Fri Mar 16 2018 Mohamed El Morabity <melmorabity@fedoraproject.org> - 1:3.3.0-1
- Update to latest stable release for Kodi 18

* Thu Mar 01 2018 RPM Fusion Release Engineering <leigh123linux@googlemail.com> - 1:2.4.5-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Tue Oct 03 2017 Mohamed El Morabity <melmorabity@fedoraproject.org> - 1:2.4.5-1
- Update to 2.4.5

* Fri Apr 28 2017 Mohamed El Morabity <melmorabity@fedorapeople.org> - 1:2.4.3-1
- Update to latest stable release for Kodi 17

* Sun Jul 24 2016 Mohamed El Morabity <melmorabity@fedoraproject.org> - 1:1.11.9-1
- Update to latest stable release for Kodi 16

* Mon Aug 24 2015 Mohamed El Morabity <melmorabity@fedoraproject.org> - 1:1.10.7-1
- Initial RPM release
