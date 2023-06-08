Summary:	Small basic interpreter with printing and graphics
Name:		yabasic
Version:	2.90.3
Release:	1
License:	Artistic
Group:		Development/Other
Source0:	http://www.yabasic.de/download/%{name}-%{version}.tar.gz
URL:		http://www.yabasic.de/
BuildRequires:	pkgconfig(x11)
BuildRequires:	pkgconfig(xt)
BuildRequires:	ncurses-devel

%description
Yabasic implements the most common and simple elements of the basic
language; It comes with for-loops and goto with while-loops and
procedures. Yabasic does monochrome line grafics, printing comes with
no extra effort. Yabasic runs under Unix and Windows; it is small
(less than 200KB) and free.

%prep
%setup -q
autoreconf -fi
%configure

%build
%make_build

%check
make check-TESTS

%install
%make_install

%files
%defattr(-,root,root)
%doc AUTHORS NEWS README *.htm ChangeLog
%{_bindir}/*
%{_mandir}/man1/yabasic.*
