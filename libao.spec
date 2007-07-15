%define	name	libao
%define	version	0.8.6
%define release %mkrel 3

%define	libname	%mklibname ao 2

Name:		%{name}
Summary:	Cross Platform Audio Output Library
Version:	%{version}
Release:	%{release}
Group:		System/Libraries
License:	GPL
URL:		http://www.xiph.org/ao/
Source0:	http://downloads.xiph.org/releases/ao/%{name}-%{version}.tar.bz2
Patch0:		libao-0.8.4-fix-optflags.patch.bz2
Patch1:		libao-0.8.3-lib64.patch.bz2
# gw raise priority of alsa09 over arts
Patch2: libao-0.8.6-priority.patch.bz2
BuildRoot:	%{_tmppath}/%{name}-%{version}-%{release}-buildroot
BuildRequires:	arts esound-devel alsa-lib-devel perl arts-devel
#BuildRequires:	libpolypaudio-devel
BuildRequires:	automake1.8
%define _requires_exceptions libartsc.so\\|libesd.so\\|libaudiofile.so\\|libaudio.so\\|libpolyp

%description
Libao is a cross platform audio output library. It currently supports ESD,
OSS, Solaris, and IRIX.

%package -n	%{libname}
Summary:	Main library for %{name}
Group:		System/Libraries

%description -n	%{libname}
This package contains the library needed to run programs dynamically
linked with %{name}.

%package -n	%{libname}-devel
Summary:	Headers for developing programs that will use %{name}
Group:		Development/C
Requires:	%{libname} = %{version}
Provides:	%{name}-devel = %{version}-%{release}

%description -n	%{libname}-devel
This package contains the headers that programmers will need to develop
applications which will use %{name}.

%prep
%setup -q
%patch0 -p0 -b .optflags
%patch1 -p1 -b .lib64
%patch2 -p1 -b .priority
ACLOCAL=aclocal-1.8 AUTOMAKE=automake-1.8 autoreconf --force --install

%build
%configure2_5x --disable-polyp
%make

%install
rm -rf $RPM_BUILD_ROOT
%makeinstall_std
rm -rf $RPM_BUILD_ROOT%{_docdir}
install -d -m 755 $RPM_BUILD_ROOT%{_libdir}/%{name}/

%clean 
rm -rf $RPM_BUILD_ROOT

%post -n %{libname} -p /sbin/ldconfig
%postun -n %{libname} -p /sbin/ldconfig

%files -n %{libname}
%defattr(-,root,root)
%doc AUTHORS COPYING README
%{_libdir}/libao.so.*
%{_libdir}/ao/*
%{_mandir}/man5/*

%files -n %{libname}-devel
%defattr(-,root,root)
%doc CHANGES doc/*.{html,c,css}
%{_includedir}/ao
%{_libdir}/libao.so
%{_libdir}/libao.la
%dir %{_libdir}/%{name}/
%{_datadir}/aclocal/ao.m4
%{_libdir}/pkgconfig/*
