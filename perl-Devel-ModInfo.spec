
# Conditional build:
%bcond_without	tests	# do perform "make test"

%include	/usr/lib/rpm/macros.perl
%define	pdir	Devel
%define	pnam	ModInfo
Summary:	Devel::ModInfo - ModInfo is a system for documenting your Perl modules without creating runtime overhead.
Name:		perl-Devel-ModInfo
Version:	0.05
Release:	1
# same as perl
License:	GPL/Artistic
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/%{pdir}/%{pdir}-%{pnam}-%{version}.tar.gz
# Source0-md5:	68b98713efba6de10af41bde55777b04
BuildRequires:	perl-devel >= 5.6
BuildRequires:	rpm-perlprov >= 4.1-13
BuildRequires:  perl(XML::DOM)
%if %{with tests}
%endif
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
ModInfo is a system for documenting your Perl modules without
creating runtime overhead.  Some of the concepts are based on
the JavaBean BeanInfo API, but the implementation is specific 
to Perl, and does not require extra coding.

%prep
%setup -q -n %{pdir}-%{pnam}-%{version}

%build
%{__perl} Makefile.PL \
	INSTALLDIRS=vendor

%{__make}

%{?with_tests:make test}

%install
rm -rf $RPM_BUILD_ROOT
make install DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%dir %{perl_vendorlib}/%{pdir}/%{pnam}
%attr(755,root,root) %{_bindir}/*
%{perl_vendorlib}/%{pdir}/%{pnam}.pm
%{perl_vendorlib}/%{pdir}/%{pnam}/*.pm
%{perl_vendorlib}/%{pdir}/%{pnam}/ParamHash/*.pm
%{perl_vendorlib}/%{pdir}/%{pnam}/Tutorial.pod
%{perl_vendorlib}/auto/%{pdir}/%{pnam}/autosplit.ix
%{_mandir}/man[13]/*
