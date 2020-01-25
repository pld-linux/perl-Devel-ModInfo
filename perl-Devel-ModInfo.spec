#
# Conditional build:
%bcond_without	tests	# do perform "make test"

%define		pdir	Devel
%define		pnam	ModInfo
Summary:	Devel::ModInfo - documenting system for Perl modules without creating runtime overhead
Summary(pl.UTF-8):	Devel::ModInfo - system dokumentacji modułów Perla bez narzutu w czasie wykonywania
Name:		perl-Devel-ModInfo
Version:	0.05
Release:	3
License:	Artistic
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/%{pdir}/%{pdir}-%{pnam}-%{version}.tar.gz
# Source0-md5:	68b98713efba6de10af41bde55777b04
URL:		http://search.cpan.org/dist/Devel-ModInfo/
BuildRequires:	perl-devel >= 1:5.8.0
BuildRequires:	rpm-perlprov >= 4.1-13
%if %{with tests}
BuildRequires:	perl-Parse-RecDescent
BuildRequires:	perl-XML-DOM
%endif
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
ModInfo is a system for documenting your Perl modules without creating
runtime overhead. Some of the concepts are based on the JavaBean
BeanInfo API, but the implementation is specific to Perl, and does not
require extra coding.

%description -l pl.UTF-8
ModInfo to system dokumentacji dla modułów Perla bez tworzenia narzutu
w czasie wykonywania. Niektóre idee są oparte na API JavaBean
BeanInfo, ale implementacja jest specyficzna dla Perla i nie wymaga
dodatkowego kodowania.

%prep
%setup -q -n %{pdir}-%{pnam}-%{version}

%build
%{__perl} Makefile.PL \
	INSTALLDIRS=vendor

%{__make}

%{?with_tests:%{__make} test}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc Changes README
%attr(755,root,root) %{_bindir}/*
%{perl_vendorlib}/Devel/ModInfo.pm
%dir %{perl_vendorlib}/Devel/ModInfo
%{perl_vendorlib}/Devel/ModInfo/*.pm
%{perl_vendorlib}/Devel/ModInfo/ParamHash
%dir %{perl_vendorlib}/auto/Devel/ModInfo
%{perl_vendorlib}/auto/Devel/ModInfo/autosplit.ix
%{_mandir}/man[13]/*
