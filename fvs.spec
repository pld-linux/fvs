Summary:	Fingerprint Verification System
Summary(pl):	Fingerprint Verifycation System - system weryfikacji odcisków palców
Name:		fvs
Version:	0.1.0
Release:	1
Epoch:		1
License:	MPL 1.1
Group:		Libraries
Source0:	http://dl.sourceforge.net/fvs/%{name}-%{version}.tar.bz2
# Source0-md5:	dba7993ac4d3a21c70ce058e34dac7b3
URL:		http://fvs.sourceforge.net/
BuildRequires:	ImageMagick-devel
Obsoletes:	fvs-gfvs
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
Requires:	%{name} = %{epoch}:%{version}

%description devel
Header files for FVS library.

%description devel -l pl
Pliki nag³ówkowe biblioteki FVS.

%package static
Summary:	Static FVS library
Summary(pl):	Statyczna biblioteka FVS
Group:		Development/Libraries
Requires:	%{name}-devel = %{epoch}:%{version}

%description static
Static FVS library.

%description static -l pl
Statyczna biblioteka FVS.

%prep
%setup -q

%build
%configure
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
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
