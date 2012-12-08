%define _disable_ld_no_undefined 1
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
BuildRequires:	pkgconfig(alsa)
BuildRequires:	pkgconfig(libpulse)

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
%makeinstall_std
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


%changelog
* Tue Dec 27 2011 Matthew Dawkins <mattydaw@mandriva.org> 1.1.0-1
+ Revision: 745493
- build fix
- p0 applied upstream
- new version 1.1.0
- cleaned up spec a bit

* Mon May 02 2011 Oden Eriksson <oeriksson@mandriva.com> 1.0.0-6
+ Revision: 662346
- mass rebuild

* Sun Feb 20 2011 Александр Казанцев <kazancas@mandriva.org> 1.0.0-5
+ Revision: 639038
- fix PulseAudio plugin bug

* Sun Nov 28 2010 Oden Eriksson <oeriksson@mandriva.com> 1.0.0-4mdv2011.0
+ Revision: 602518
- rebuild

* Wed Apr 28 2010 Emmanuel Andry <eandry@mandriva.org> 1.0.0-3mdv2010.1
+ Revision: 540202
- drop esound support

* Tue Apr 06 2010 Guillaume Rousse <guillomovitch@mandriva.org> 1.0.0-2mdv2010.1
+ Revision: 532347
- rebuild

* Sat Mar 27 2010 Funda Wang <fwang@mandriva.org> 1.0.0-1mdv2010.1
+ Revision: 528105
- new version 1.0.0
- drop upstream merged patches
- drop arts patch, we don't have it any more

* Tue Mar 16 2010 Oden Eriksson <oeriksson@mandriva.com> 0.8.8-10mdv2010.1
+ Revision: 520747
- rebuilt for 2010.1

* Wed Sep 02 2009 Christophe Fergeau <cfergeau@mandriva.com> 0.8.8-9mdv2010.0
+ Revision: 425513
- rebuild

* Mon Feb 09 2009 Helio Chissini de Castro <helio@mandriva.com> 0.8.8-8mdv2009.1
+ Revision: 338935
- Adios arts

* Tue Jun 17 2008 Thierry Vignaud <tv@mandriva.org> 0.8.8-7mdv2009.0
+ Revision: 222429
- rebuild

  + Pixel <pixel@mandriva.com>
    - do not call ldconfig in %%post/%%postun, it is now handled by filetriggers

* Thu Feb 07 2008 Frederic Crozat <fcrozat@mandriva.com> 0.8.8-6mdv2008.1
+ Revision: 163705
- Update patch4 to bump pulse priority from 47 to 50 (should be multiple of 5)

* Thu Feb 07 2008 Frederic Crozat <fcrozat@mandriva.com> 0.8.8-5mdv2008.1
+ Revision: 163628
- Patch3: favor pulse over ALSA if present (Mandriva bug #36965)

* Wed Feb 06 2008 Frederic Crozat <fcrozat@mandriva.com> 0.8.8-4mdv2008.1
+ Revision: 163126
- Patch3 (SVN): fix handling buffer for alsa plugin
- remove invalid CFLAGS set to -O20, use our own cflags

* Sun Jan 13 2008 Thierry Vignaud <tv@mandriva.org> 0.8.8-3mdv2008.1
+ Revision: 150447
- rebuild
- kill re-definition of %%buildroot on Pixel's request

  + Olivier Blin <blino@mandriva.org>
    - restore BuildRoot

* Mon Aug 06 2007 David Walluck <walluck@mandriva.org> 0.8.8-2mdv2008.0
+ Revision: 59536
- move %%{_mandir}/man5/* to devel package in order to avoid multiarch conflict
- bunzip2 patches
- use original archive

* Mon Jul 16 2007 Tomasz Pawel Gajc <tpg@mandriva.org> 0.8.8-1mdv2008.0
+ Revision: 52750
- new version
- drop patches 0 and 1
- adjust buildrequires
- enable pulseaudio support
- enable alsa mmap support
- spec file clean

* Mon Jul 16 2007 Adam Williamson <awilliamson@mandriva.org> 0.8.6-4mdv2008.0
+ Revision: 52714
- rebuild for 2008
- unversion automake dependency
- new devel policy
- Import libao



* Tue Jul 25 2006 G�tz Waschk <waschk@mandriva.org> 0.8.6-3mdv2007.0
- raise priority of alsa plugin

* Wed May  3 2006 G�tz Waschk <waschk@mandriva.org> 0.8.6-2mdk
- disable polypaudio

* Thu Dec  8 2005 G�tz Waschk <waschk@mandriva.org> 0.8.6-1mdk
- support polypaudio
- fix source URL
- drop merged patch 2
- New release 0.8.6
- use mkrel

* Tue Mar 15 2005 Olivier Blin <oblin@mandrakesoft.com> 0.8.5-4mdk
- own %%{_libdir}/%%{name}/ directory

* Sun Dec 26 2004 Abel Cheung <deaddog@mandrake.org> 0.8.5-3mdk
- Simplify variables
- P2: Fix warning related to automake 1.8

* Sat Jul 10 2004 G�tz Waschk <waschk@linux-mandrake.com> 0.8.5-2mdk
- rebuild for new alsa

* Sat May 29 2004 Per �yvind Karlsen <peroyvind@linux-mandrake.com> 0.8.5-1mdk
- 0.8.5
- drop P2 as alsa 1.0 is now supported upstream
- updated url
- spec cosmetics

* Fri Dec 12 2003 G�tz Waschk <waschk@linux-mandrake.com> 0.8.4-3mdk
- fix buildrequires

* Fri Dec 12 2003 Guillaume Cottenceau <gc@mandrakesoft.com> 0.8.4-2mdk
- allow build against alsa-1.0 by asking for old API
- better find_requires exceptions handling

* Thu Dec 11 2003 Guillaume Cottenceau <gc@mandrakesoft.com> 0.8.4-1mdk
- new version

* Thu Sep  4 2003 Guillaume Cottenceau <gc@mandrakesoft.com> 0.8.3-8mdk
- fixes invalid-build-requires libarts2-devel

* Tue Sep  2 2003 Guillaume Cottenceau <gc@mandrakesoft.com> 0.8.3-7mdk
- mklibname

* Mon Sep  1 2003 Guillaume Cottenceau <gc@mandrakesoft.com> 0.8.3-6mdk
- remove temporarily libarts because it makes gcompris and xmmsao
  crash for some users

* Sat Jul 26 2003 Per �yvind Karlsen <peroyvind@sintrax.net> 0.8.3-5mdk
- rebuild
- use %%make macro
- use %%makeinstall_std macro

* Tue Jul  8 2003 Guillaume Cottenceau <gc@mandrakesoft.com> 0.8.3-4mdk
- rebuild for new devel provides

* Tue May 13 2003 Guillaume Cottenceau <gc@mandrakesoft.com> 0.8.3-3mdk
- rebuild 

* Thu Jul 25 2002 Gwenole Beauchesne <gbeauchesne@mandrakesoft.com> 0.8.3-2mdk
- Patch1: lib64 fixes to ao.m4

* Fri Jul 19 2002 Guillaume Cottenceau <gc@mandrakesoft.com> 0.8.3-1mdk
- new version
- patch #1 integrated upstream

* Mon Apr 29 2002 Guillaume Cottenceau <gc@mandrakesoft.com> 0.8.2-3mdk
- rebuild for new alsa

* Mon Jan 14 2002 Guillaume Cottenceau <gc@mandrakesoft.com> 0.8.2-2mdk
- have libao.la file (I suck)

* Fri Jan 11 2002 Guillaume Cottenceau <gc@mandrakesoft.com> 0.8.2-1mdk
- new version
- merge RH version:
  - idea of external special requires computation so that we don't blindly
    have unecessary requires on arts/esd/audiofile
  - patch #1 to correctly depend on libdl
  - man page has nothing to do in devel package, have it in main package

* Tue Oct 16 2001 Guillaume Cottenceau <gc@mandrakesoft.com> 0.8.0-4mdk
- fix obsolete-tag Copyright
- fix strange-permission

* Mon Aug 27 2001 Guillaume Cottenceau <gc@mandrakesoft.com> 0.8.0-3mdk
- fix buildrequires

* Mon Aug 20 2001 Guillaume Cottenceau <gc@mandrakesoft.com> 0.8.0-2mdk
- added man page to the devel package
    by Gotz Waschk <waschk@linux-mandrake.com>

* Tue Aug 14 2001 Guillaume Cottenceau <gc@mandrakesoft.com> 0.8.0-1mdk
- new version
- patch1 integrated upstream
- fix non-versioned-file-in-library-package

* Sat Jun 23 2001 Guillaume Cottenceau <gc@mandrakesoft.com> 0.7.0-1mdk
- new version

* Thu Apr 12 2001 Guillaume Cottenceau <gc@mandrakesoft.com> 0.6.0-2mdk
- don't forever block on a busy dsp

* Fri Mar  9 2001 Guillaume Cottenceau <gc@mandrakesoft.com> 0.6.0-1mdk
- 0.6.0
- fix provides
- fix buildrequires

* Mon Dec 11 2000 Guillaume Cottenceau <gc@mandrakesoft.com> 0.5.0-2mdk
- fixes optflags

* Mon Nov 27 2000 Guillaume Cottenceau <gc@mandrakesoft.com> 0.5.0-1mdk
- Package for Linux-Mandrake

* Sun Sep 03 2000 Jack Moffitt <jack@icecast.org>
- initial spec file created
