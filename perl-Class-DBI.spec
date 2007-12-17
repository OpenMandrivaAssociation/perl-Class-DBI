%define module  Class-DBI
%define name    perl-%{module}
%define version 3.0.17
%define release %mkrel 1

Name:           %{name}
Version:        %{version}
Release:        %{release}
Summary:        Simple Database Abstraction
License:        GPL or Artistic
Group:          Development/Perl
Url:            http://search.cpan.org/dist/%{module}
Source:         http://www.cpan.org/modules/by-module/Class/%{module}-v%{version}.tar.bz2
%if %{mdkversion} < 1010
BuildRequires:  perl-devel
%endif
BuildRequires:  perl(Class::Trigger)
BuildRequires:  perl(Class::Accessor)
BuildRequires:  perl(Class::Data::Inheritable)
BuildRequires:  perl(Clone)
BuildRequires:  perl(Ima::DBI)
BuildRequires:  perl(UNIVERSAL::moniker)
BuildRequires:  perl-version
Requires:       perl-version
BuildArch:      noarch

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
%setup -q -n %{module}-v%{version} 

%build
%{__perl} Makefile.PL INSTALLDIRS=vendor
%make

%check
%{__make} test

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


