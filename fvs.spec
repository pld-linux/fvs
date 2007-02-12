Summary:	Fingerprint Verification System
Summary(pl.UTF-8):   Fingerprint Verifycation System - system weryfikacji odcisków palców
Name:		fvs
Version:	0.1.1
Release:	1
Epoch:		1
License:	MPL 1.1
Group:		Libraries
Source0:	http://dl.sourceforge.net/fvs/%{name}-%{version}.tar.bz2
# Source0-md5:	f369e2f47f900712230576b56e7aaef1
URL:		http://fvs.sourceforge.net/
BuildRequires:	ImageMagick-devel
BuildRequires:	automake
Obsoletes:	fvs-gfvs
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
This library provides a framework to use when creating a fingerprint
recognition program. It provides easy to use interfaces to load
fingerprint files, process fingerprint images and analyse the data.

%description -l pl.UTF-8
Ta biblioteka udostępnia szkielet, który można wykorzystać przy
tworzeniu programów rozpoznających odciski palców. Dostarcza łatwy w
użyciu interfejs do wczytywania plików z odciskami, przetwarzania tych
obrazów i analizy danych.

%package devel
Summary:	Header files for FVS library
Summary(pl.UTF-8):   Pliki nagłówkowe biblioteki FVS
Group:		Development/Libraries
Requires:	%{name} = %{epoch}:%{version}-%{release}

%description devel
Header files for FVS library.

%description devel -l pl.UTF-8
Pliki nagłówkowe biblioteki FVS.

%package static
Summary:	Static FVS library
Summary(pl.UTF-8):   Statyczna biblioteka FVS
Group:		Development/Libraries
Requires:	%{name}-devel = %{epoch}:%{version}-%{release}

%description static
Static FVS library.

%description static -l pl.UTF-8
Statyczna biblioteka FVS.

%prep
%setup -q

# hack for broken sources
touch fvs

%build
cp -f /usr/share/automake/config.* .
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
%doc doc/{*.css,*.html,images}
%attr(755,root,root) %{_libdir}/lib*.so
%{_libdir}/lib*.la
%{_includedir}/fvs

%files static
%defattr(644,root,root,755)
%{_libdir}/lib*.a
