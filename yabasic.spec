%define name yabasic
%define version 2.763
%define release %mkrel 7

Summary:	Small basic interpreter with printing and graphics
Name:		%{name}
Version:	%{version}
Release:	%{release}
License:	Artistic
Group:		Development/Other
Source0:	http://www.yabasic.de/download/%{name}-%{version}.tar.bz2
URL:		http://www.yabasic.de/
BuildRequires:	pkgconfig(x11)
BuildRequires:	pkgconfig(xt)
BuildRequires:	ncurses-devel
BuildRoot:	%{_tmppath}/%{name}-buildroot

%description
Yabasic implements the most common and simple elements of the basic
language; It comes with for-loops and goto with while-loops and
procedures. Yabasic does monochrome line grafics, printing comes with
no extra effort. Yabasic runs under Unix and Windows; it is small
(less than 200KB) and free.

%prep
%setup -q

%build
autoreconf -fi
%configure2_5x
%make

%check
make check-TESTS

%install
rm -rf $RPM_BUILD_ROOT

%makeinstall_std

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,root)
%doc AUTHORS NEWS README *.htm ChangeLog
%{_bindir}/*
%{_mandir}/man1/yabasic.*


%changelog
* Fri Jan 21 2011 Funda Wang <fwang@mandriva.org> 2.763-7mdv2011.0
+ Revision: 632006
- simplify BR

  + Thierry Vignaud <tv@mandriva.org>
    - rebuild

* Mon Aug 04 2008 Thierry Vignaud <tv@mandriva.org> 2.763-6mdv2009.0
+ Revision: 262760
- rebuild

* Thu Jul 31 2008 Thierry Vignaud <tv@mandriva.org> 2.763-5mdv2009.0
+ Revision: 257854
- rebuild

* Fri Dec 21 2007 Olivier Blin <oblin@mandriva.com> 2.763-3mdv2008.1
+ Revision: 136631
- restore BuildRoot

  + Thierry Vignaud <tv@mandriva.org>
    - kill re-definition of %%buildroot on Pixel's request
    - buildrequires X11-devel instead of XFree86-devel

* Wed Aug 22 2007 Olivier Thauvin <nanardon@mandriva.org> 2.763-3mdv2008.0
+ Revision: 68894
- rebuild

  + Thierry Vignaud <tv@mandriva.org>
    - fix man pages extension


* Thu Aug 10 2006 Olivier Thauvin <nanardon@mandriva.org>
+ 08/10/06 10:31:51 (55329)
- rebuild

* Thu Aug 10 2006 Olivier Thauvin <nanardon@mandriva.org>
+ 08/10/06 10:30:17 (55328)
Import yabasic

* Mon Oct 17 2005 Olivier Thauvin <nanardon@mandriva.org> 2.763-1mdk
- 2.763

* Sun May 01 2005 Olivier Thauvin <nanardon@mandriva.org> 2.751-1mdk
- 2.751
- add %%check section

* Fri May 14 2004 Olivier Thauvin <thauvin@aerov.jussieu.fr> 2.744-1mdk
- 2.744

