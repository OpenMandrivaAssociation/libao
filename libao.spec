%define _disable_ld_no_undefined 1

%define	major	4
%define	libname	%mklibname ao %{major}
%define	devname	%mklibname ao -d

Name:		libao
Summary:	Cross Platform Audio Output Library
Version:	1.2.2
Release:	2
Group:		System/Libraries
License:	GPL
URL:		https://www.xiph.org/ao/
#Source0:	http://downloads.xiph.org/releases/ao/%{name}-%{version}.tar.gz
Source0:	https://github.com/xiph/%{name}/archive/%{version}/%{name}-%{version}.tar.gz
Patch0:		libao-1.2.2-linking.patch
Patch1:		libao-1.2.2-CVE-2017-11548.patch
BuildRequires:	pkgconfig(alsa)
BuildRequires:	pkgconfig(libpulse)

%description
Libao is a cross-platform audio library that allows programs 
to output audio using a simple API on a wide variety of platforms. 
It currently supports:

- ALSA
- pulseaudio
- OSS

%package -n	%{libname}
Summary:	Main library for %{name}
Group:		System/Libraries

%description -n	%{libname}
This package contains the library needed to run programs dynamically
linked with %{name}.

%package -n	%{devname}
Summary:	Headers for developing programs that will use %{name}
Group:		Development/C
Requires:	%{libname} = %{version}
Provides:	%{name}-devel = %{version}-%{release}

%description -n	%{devname}
This package contains the headers that programmers will need to develop
applications which will use %{name}.

%prep
%setup -q
%autopatch -p1

%build
autoreconf -vfi
%configure2_5x \
	--disable-esd \
	--disable-static \
	--disable-arts \
	--enable-pulse \
	--enable-alsa-mmap
	
# (Fedora) kill rpath
sed -i 's|^hardcode_libdir_flag_spec=.*|hardcode_libdir_flag_spec=""|g' libtool
sed -i 's|^runpath_var=LD_RUN_PATH|runpath_var=DIE_RPATH_DIE|g' libtool

%make_build -C src libao.la
%make_build

%install
%make_install
rm -rf %{buildroot}%{_docdir}
install -d -m 755 %{buildroot}%{_libdir}/%{name}/

%files -n %{libname}
%doc AUTHORS COPYING README
%{_libdir}/libao.so.%{major}*
%{_libdir}/ao/*

%files -n %{devname}
%doc CHANGES doc/*.{html,c,css}
%{_includedir}/ao
%{_libdir}/libao.so
%{_libdir}/ckport/db/libao.ckport
%dir %{_libdir}/%{name}/
%{_datadir}/aclocal/ao.m4
%{_libdir}/pkgconfig/*
%{_mandir}/man5/*

