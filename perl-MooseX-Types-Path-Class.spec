#
# Conditional build:
%bcond_without	tests		# do not perform "make test"
#
%include	/usr/lib/rpm/macros.perl
%define	pdir	MooseX
%define	pnam	Types-Path-Class
Summary:	MooseX::Types::Path::Class - A Path::Class type library for Moose
Summary(pl.UTF-8):	MooseX::Types::Path::Class - biblioteka typu Path::Class dla Moose
Name:		perl-MooseX-Types-Path-Class
Version:	0.05
Release:	1
License:	GPL v1+ or Artistic
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/MooseX/%{pdir}-%{pnam}-%{version}.tar.gz
# Source0-md5:	79a0d19fe8b4547b232605645c75aaad
URL:		http://search.cpan.org/dist/MooseX-Types-Path-Class/
BuildRequires:	perl-devel >= 1:5.8.0
BuildRequires:	rpm-perlprov >= 4.1-13
%if %{with tests}
BuildRequires:	perl-Class-MOP
BuildRequires:	perl-Moose >= 0.39
BuildRequires:	perl-MooseX-Types >= 0.04
BuildRequires:	perl-Path-Class >= 0.16
%endif
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
MooseX::Types::Path::Class creates common Moose types, coercions and
option specifications useful for dealing with Path::Class objects as
Moose attributes.

Coercions (see Moose::Util::TypeConstraints) are made from both 'Str'
and 'ArrayRef' to both Path::Class::Dir and Path::Class::File objects.
If you have MooseX::Getopt installed, the Getopt option type ("=s")
will be added for both Path::Class::Dir and Path::Class::File.

%description -l pl.UTF-8
MooseX::Types::Path::Class tworzy wspólne typy Moose, konieczne i
pocjonalne specyfikacje użyteczne do radzenia sobnie z obiektami
Path:Class jako atrybutami Moose.

%prep
%setup -q -n %{pdir}-%{pnam}-%{version}

%build
%{__perl} Makefile.PL \
	INSTALLDIRS=vendor
%{__make}

%{?with_tests:%{__make} test}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} pure_install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc Changes README
%{perl_vendorlib}/MooseX/Types/Path/*.pm
%{_mandir}/man3/*
