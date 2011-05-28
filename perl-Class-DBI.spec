%define upstream_name    Class-DBI
%define upstream_version 3.0.17

Name:       perl-%{upstream_name}
Version:    %perl_convert_version %{upstream_version}
Release:    %mkrel 6

Summary:    Simple Database Abstraction
License:    GPL+ or Artistic
Group:      Development/Perl
Url:        http://search.cpan.org/dist/%{upstream_name}
Source0:    http://www.cpan.org/modules/by-module/Class/%{upstream_name}-v%{upstream_version}.tar.bz2

%if %{mdkversion} < 1010
BuildRequires:  perl-devel
%endif
BuildRequires:  perl(Class::Accessor)
BuildRequires:  perl(Class::Data::Inheritable)
BuildRequires:  perl(Class::Trigger)
BuildRequires:  perl(Clone)
BuildRequires:  perl(DBIx::ContextualFetch)
BuildRequires:  perl(Ima::DBI)
BuildRequires:  perl(UNIVERSAL::moniker)
BuildRequires:  perl(version)

BuildArch:      noarch
BuildRoot:      %{_tmppath}/%{name}-%{version}-%{release}

Requires:       perl(version)

%description
Class::DBI provides a convenient abstraction layer to a database.

It not only provides a simple database to object mapping layer, but can be used
to implement several higher order database functions (triggers, referential
integrity, cascading delete etc.), at the application level, rather than at the
database.

This is particularly useful when using a database which doesn't support these
(such as MySQL), or when you would like your code to be portable across
multiple databases which might implement these things in different ways.

In short, Class::DBI aims to make it simple to introduce 'best practice' when
dealing with data stored in a relational database.

%prep
%setup -q -n %{upstream_name}-v%{upstream_version}

%build
%{__perl} Makefile.PL INSTALLDIRS=vendor
%make

%check
%make test

%install
rm -rf %{buildroot}
%makeinstall_std

%clean 
rm -rf %{buildroot}

%files
%defattr(-,root,root)
%doc Changes README
%{perl_vendorlib}/Class
%{_mandir}/*/*
