%define __strip %{_mingw32_strip}
%define __objdump %{_mingw32_objdump}
%define _use_internal_dependency_generator 0
%define __find_requires %{_mingw32_findrequires}
%define __find_provides %{_mingw32_findprovides}

Name:           mingw32-pixman
Version:        0.13.2
Release:        4
Summary:        MinGW Windows Pixman library

License:        MIT
URL:            http://xorg.freedesktop.org/
Group:          Development/Other

Source0:        http://xorg.freedesktop.org/archive/individual/lib/pixman-%{version}.tar.gz
Source1:        make-pixman-snapshot.sh

Patch0:         pixman-0.13.2-license.patch

BuildArch:      noarch

BuildRequires:  mingw32-filesystem >= 23
BuildRequires:  mingw32-gcc
BuildRequires:  mingw32-binutils
BuildRequires:  mingw32-dlfcn

Requires:       pkgconfig

%description
MinGW Windows Pixman library.


%prep
%setup -q -n pixman-%{version}
%patch0 -p1


%build
# Uses GTK for its testsuite, so disable this otherwise
# we have a chicken & egg problem on mingw
%{_mingw32_configure} --disable-gtk --disable-static
%make

%install
%makeinstall_std


%files
%doc LICENSE
%{_mingw32_bindir}/libpixman-1-0.dll
%{_mingw32_includedir}/pixman-1
%{_mingw32_libdir}/libpixman-1.dll.a
%{_mingw32_libdir}/pkgconfig/pixman-1.pc


%changelog
* Fri Dec 10 2010 Oden Eriksson <oeriksson@mandriva.com> 0.13.2-3mdv2011.0
+ Revision: 620355
- the mass rebuild of 2010.0 packages

* Mon Sep 14 2009 Thierry Vignaud <tv@mandriva.org> 0.13.2-2mdv2010.0
+ Revision: 439930
- rebuild

* Wed Feb 18 2009 Jérôme Soyer <saispo@mandriva.org> 0.13.2-1mdv2009.1
+ Revision: 342301
- Fix typo
- import mingw32-pixman


