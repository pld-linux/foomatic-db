%include	/usr/lib/rpm/macros.perl
Summary:	Foomatic database
Summary(pl):	Baza danych dla foomatic
Name:		foomatic-db
Version:	20040209
Release:	1
License:	GPL
Group:		Applications/System
Source0:	http://www.linuxprinting.org/download/foomatic/%{name}-%{version}.tar.gz
# Source0-md5:	34875a301c0c1765d3da45a8c21224da
URL:		http://www.linuxprinting.org/foomatic.html
BuildRequires:	autoconf
BuildRequires:	automake
Requires:	foomatic-db-engine >= 3.0.1
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
The collected knowledge about printers, drivers, and driver options in
XML files, used by foomatic-db-engine to generate PPD files.

%description -l pl
Ca�o�ciowa informacja o drukarkach, sterownikach i opcjach sterownik�w
w postaci plik�w XML, u�ywanych przez foomatic-db-engine do generowania
plik�w PPD.

%prep
%setup -q

%build
%{__aclocal}
%{__autoconf}
%configure
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc ChangeLog TODO README USAGE
%{_datadir}/foomatic/db/source/driver/*
%{_datadir}/foomatic/db/source/opt/*
%{_datadir}/foomatic/db/source/printer/*
