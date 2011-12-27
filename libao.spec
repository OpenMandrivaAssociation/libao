%define _requires_exceptions libasound.so\\|libesd.so\\|libaudiofile.so\\|libaudio.so\\|libpulse

%define major 4
%define	libname		%mklibname ao %{major}
%define develname	%mklibname ao -d

Name:		libao
Summary:	Cross Platform Audio Output Library
Version:	1.1.0
Release:	1
Group:		System/Libraries
License:	GPL
URL:		http://www.xiph.org/ao/
Source0:	http://downloads.xiph.org/releases/ao/%{name}-%{version}.tar.gz
BuildRequires:	libalsa-devel
BuildRequires:	libpulseaudio-devel

%description
Libao is a cross-platform audio library that allows programs 
to output audio using a simple API on a wide variety of platforms. 
It currently supports:

- ALSA
- Esound
- pulseaudio
- OSS

%package -n	%{libname}
Summary:	Main library for %{name}
Group:		System/Libraries

%description -n	%{libname}
This package contains the library needed to run programs dynamically
linked with %{name}.

%package -n	%{develname}
Summary:	Headers for developing programs that will use %{name}
Group:		Development/C
Requires:	%{libname} = %{version}
Provides:	%{name}-devel = %{version}-%{release}
Obsoletes:	%mklibname ao 2 -d

%description -n	%{develname}
This package contains the headers that programmers will need to develop
applications which will use %{name}.

%prep
%setup -q

# remove incorrect flags, optflag will be used instead
sed -i "s/-O20//" configure

%build
%configure2_5x \
	--disable-static \
	--disable-esound \
	--disable-arts \
	--enable-pulseaudio \
	--enable-alsa09-mmap

%make

%install
rm -rf %{buildroot}
%makeinstall_std
find %{buildroot} -type f -name "*.la" -exec rm -f {} ';'
rm -rf %{buildroot}%{_docdir}
install -d -m 755 %{buildroot}%{_libdir}/%{name}/

%files -n %{libname}
%doc AUTHORS COPYING README
%{_libdir}/libao.so.%{major}*
%{_libdir}/ao/*

%files -n %{develname}
%doc CHANGES doc/*.{html,c,css}
%{_includedir}/ao
%{_libdir}/libao.so
%dir %{_libdir}/%{name}/
%{_datadir}/aclocal/ao.m4
%{_libdir}/pkgconfig/*
%{_mandir}/man5/*
