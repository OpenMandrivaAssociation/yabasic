%define name yabasic
%define version 2.763
%define release %mkrel 3

Summary:	Small basic interpreter with printing and graphics
Name:		%{name}
Version:	%{version}
Release:	%{release}
License:	Artistic
Group:		Development/Other
Source0:	http://www.yabasic.de/download/%{name}-%{version}.tar.bz2
URL:		http://www.yabasic.de/
BuildRequires:	bison
BuildRequires:	flex
BuildRequires:	automake
BuildRequires:	autoconf >= 2.13
BuildRequires:	libtool
BuildRequires:	X11-devel
BuildRequires:	ncurses-devel

%description
Yabasic implements the most common and simple elements of the basic
language; It comes with for-loops and goto with while-loops and
procedures. Yabasic does monochrome line grafics, printing comes with
no extra effort. Yabasic runs under Unix and Windows; it is small
(less than 200KB) and free.

%prep
%setup  -q

%build
# rm -f missing
libtoolize --copy --force
aclocal
autoheader
autoconf
automake -a -c -i
%configure
%make

%check
make check-TESTS

%install
rm -rf $RPM_BUILD_ROOT

%makeinstall

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,root)
%doc AUTHORS NEWS README *.htm ChangeLog
%{_bindir}/*
%{_mandir}/man1/yabasic.*
