%define upstream_name    Class-DBI
%define upstream_version 3.0.17

Name:		perl-%{upstream_name}
Version:	%perl_convert_version %{upstream_version}
Release:	7

Summary:	Simple Database Abstraction
License:	GPL+ or Artistic
Group:		Development/Perl
Url:		http://search.cpan.org/dist/%{upstream_name}
Source0:	http://www.cpan.org/modules/by-module/Class/%{upstream_name}-v%{upstream_version}.tar.bz2

BuildRequires:	perl-devel
BuildRequires:	perl(Class::Accessor)
BuildRequires:	perl(Class::Data::Inheritable)
BuildRequires:	perl(Class::Trigger)
BuildRequires:	perl(Clone)
BuildRequires:	perl(DBIx::ContextualFetch)
BuildRequires:	perl(Ima::DBI)
BuildRequires:	perl(UNIVERSAL::moniker)
BuildRequires:	perl(version)

BuildArch:	noarch
Requires:	perl(version)

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
perl Makefile.PL INSTALLDIRS=vendor
%make

%check
%make test

%install
%makeinstall_std

%files
%doc Changes README
%{perl_vendorlib}/Class
%{_mandir}/*/*


%changelog
* Sat May 28 2011 Funda Wang <fwang@mandriva.org> 3.0.17-6mdv2011.0
+ Revision: 680787
- mass rebuild

* Sat Feb 13 2010 Jérôme Quelin <jquelin@mandriva.org> 3.0.17-5mdv2011.0
+ Revision: 505431
- adding missing buildrequires:
- rebuild using %%perl_convert_version

* Fri Sep 04 2009 Thierry Vignaud <tv@mandriva.org> 3.0.17-4mdv2010.0
+ Revision: 430325
- rebuild

* Wed Jul 30 2008 Thierry Vignaud <tv@mandriva.org> 3.0.17-3mdv2009.0
+ Revision: 255946
- rebuild
- kill re-definition of %%buildroot on Pixel's request

  + Olivier Blin <oblin@mandriva.com>
    - restore BuildRoot

* Fri Oct 12 2007 Guillaume Rousse <guillomovitch@mandriva.org> 3.0.17-1mdv2008.1
+ Revision: 97482
- update to new version 3.0.17


* Tue Nov 28 2006 Guillaume Rousse <guillomovitch@mandriva.org> 3.0.16-1mdv2007.0
+ Revision: 87843
- new version

* Thu Nov 23 2006 Guillaume Rousse <guillomovitch@mandriva.org> 3.0.14-2mdv2007.1
+ Revision: 86532
- Import perl-Class-DBI

* Tue Aug 29 2006 Guillaume Rousse <guillomovitch@mandriva.org> 3.0.14-2mdv2007.0
- Rebuild

* Sun Apr 09 2006 Arnaud de Lorbeau <devel@mandriva.com> 3.0.14-1mdk
- 3.0.14

* Thu Jan 12 2006 Rafael Garcia-Suarez <rgarciasuarez@mandriva.com> 3.0.13-1mdk
- 3.0.13
- Add perl-version in Requires

* Wed Dec 28 2005 Guillaume Rousse <guillomovitch@mandriva.org> 3.0.12-2mdk
- fix buildrequires

* Mon Dec 05 2005 Guillaume Rousse <guillomovitch@mandriva.org> 3.0.12-1mdk
- initial Mandriva package

