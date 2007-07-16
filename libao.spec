%define _requires_exceptions libartsc.so\\|libesd.so\\|libaudiofile.so\\|libaudio.so\\|libpolyp

%define	name		libao
%define	version		0.8.8
%define release		%mkrel 1

%define major 2
%define	libname		%mklibname ao %{major}
%define develname	%mklibname ao -d

Name:		%{name}
Summary:	Cross Platform Audio Output Library
Version:	%{version}
Release:	%{release}
Group:		System/Libraries
License:	GPL
URL:		http://www.xiph.org/ao/
Source0:	http://downloads.xiph.org/releases/ao/%{name}-%{version}.tar.bz2
# gw raise priority of alsa09 over arts
Patch2: 	libao-0.8.6-priority.patch.bz2
BuildRequires:	esound-devel
BuildRequires:	libalsa-devel
BuildRequires:	arts-devel
BuildRequires:	libpulseaudio-devel
BuildRoot:	%{_tmppath}/%{name}-%{version}-buildroot

%description
Libao is a cross-platform audio library that allows programs 
to output audio using a simple API on a wide variety of platforms. 
It currently supports:

- ALSA
- Esound
- aRts
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
%patch2 -p1 -b .priority

%build
%configure2_5x \
	--enable-esound \
	--enable-arts \
	--enable-pulseaudio \
	--enable-alsa09-mmap
%make

%install
rm -rf %{buildroot}
%makeinstall_std
rm -rf %{buildroot}%{_docdir}
install -d -m 755 %{buildroot}%{_libdir}/%{name}/

%clean 
rm -rf %{buildroot}

%post -n %{libname} -p /sbin/ldconfig
%postun -n %{libname} -p /sbin/ldconfig

%files -n %{libname}
%defattr(-,root,root)
%doc AUTHORS COPYING README
%{_libdir}/libao.so.%{major}*
%{_libdir}/ao/*
%{_mandir}/man5/*

%files -n %{develname}
%defattr(-,root,root)
%doc CHANGES doc/*.{html,c,css}
%{_includedir}/ao
%{_libdir}/libao.so
%{_libdir}/libao.la
%dir %{_libdir}/%{name}/
%{_datadir}/aclocal/ao.m4
%{_libdir}/pkgconfig/*
