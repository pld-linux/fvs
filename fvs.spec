Summary:	Fingerprint Verification System
Summary(pl):	Fingerprint Verifycation System - system weryfikacji odcisków palców
Name:		fvs
Version:	0.0.9
Release:	1
Epoch:		1
License:	MPL 1.1
Group:		Libraries
Source0:	http://dl.sourceforge.net/fvs/%{name}-%{version}.tar.bz2
# Source0-md5:	f886afb23665212a0b3e7abcd5b10225
Patch0:		%{name}-gfvs.patch
URL:		http://fvs.sourceforge.net/
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	gtk+2-devel >= 2.0.0
BuildRequires:	pkgconfig >= 0.9.0
BuildRequires:	libtool
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
This library provides a framework to use when creating a fingerprint
recognition program. It provides easy to use interfaces to load
fingerprint files, process fingerprint images and analyse the data.

%description -l pl
Ta biblioteka udostêpnia szkielet, który mo¿na wykorzystaæ przy
tworzeniu programów rozpoznaj±cych odciski palców. Dostarcza ³atwy w
u¿yciu interfejs do wczytywania plików z odciskami, przetwarzania tych
obrazów i analizy danych.

%package devel
Summary:	Header files for FVS library
Summary(pl):	Pliki nag³ówkowe biblioteki FVS
Group:		Development/Libraries
Requires:	%{name} = %{version}

%description devel
Header files for FVS library.

%description devel -l pl
Pliki nag³ówkowe biblioteki FVS.

%package static
Summary:	Static FVS library
Summary(pl):	Statyczna biblioteka FVS
Group:		Development/Libraries
Requires:	%{name}-devel = %{version}

%description static
Static FVS library.

%description static -l pl
Statyczna biblioteka FVS.

%package gfvs
Summary:	GUI for FVS
Summary(pl):	Graficzny interfejs do FVS
Group:		X11/Applications
Requires:	%{name} = %{version}

%description gfvs
GUI for FVS.

%description gfvs -l pl
Graficzny interfejs do FVS.

%prep
%setup -q
%patch -p1

ln -sf ../../include gfvs/src/fvs

%build
%{__libtoolize}
%{__aclocal}
%{__autoconf}
%{__autoheader}
%{__automake}
%configure
%{__make}

cd gfvs
%{__libtoolize}
%{__aclocal}
%{__autoconf}
%{__autoheader}
# no -f here
automake -a -c --foreign
%configure
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%{__make} install -C gfvs \
	DESTDIR=$RPM_BUILD_ROOT

rm -rf doc/images/.xvpics
# man3 pages not installed because of filenames (use HTML docs instead)

%clean
rm -rf $RPM_BUILD_ROOT

%post	-p /sbin/ldconfig
%postun	-p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog NEWS README TODO
%attr(755,root,root) %{_bindir}/fvs_*
%attr(755,root,root) %{_libdir}/lib*.so.*.*.*

%files devel
%defattr(644,root,root,755)
%doc doc/{html,images}
%attr(755,root,root) %{_libdir}/lib*.so
%{_libdir}/lib*.la
%{_includedir}/fvs

%files static
%defattr(644,root,root,755)
%{_libdir}/lib*.a

%files gfvs
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/gfvs
