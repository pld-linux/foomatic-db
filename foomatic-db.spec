Summary:	Foomatic database
Summary(pl.UTF-8):	Baza danych dla foomatic
Name:		foomatic-db
Version:	20251122
Release:	1
License:	GPL v2+
Group:		Applications/System
# foomatic db engine version
%define		fdbeng_ver	4.0
Source0:	https://www.linuxprinting.org/download/foomatic/%{name}-%{fdbeng_ver}-%{version}.tar.xz
# Source0-md5:	d360b72a912190b00acede3052b84ca8
URL:		https://www.linuxprinting.org/foomatic.html
BuildRequires:	bash
BuildRequires:	tar >= 1:1.22
BuildRequires:	xz
Requires:	foomatic-db-engine >= 4.0.20110615
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
The collected knowledge about printers, drivers, and driver options in
XML files, used by foomatic-db-engine to generate PPD files.

%description -l pl.UTF-8
Całościowa informacja o drukarkach, sterownikach i opcjach sterowników
w postaci plików XML, używanych przez foomatic-db-engine do
generowania plików PPD.

%prep
%setup -q

%build
%configure

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

# We don't need PPD files in this package
%{__rm} -r $RPM_BUILD_ROOT%{_datadir}/foomatic/db/source/PPD

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc ChangeLog README USAGE
%{_datadir}/foomatic/db/source/driver/*.xml
%{_datadir}/foomatic/db/source/opt/*.xml
%{_datadir}/foomatic/db/source/printer/*.xml
%{_datadir}/foomatic/db/oldprinterids
%{_datadir}/foomatic/xmlschema
