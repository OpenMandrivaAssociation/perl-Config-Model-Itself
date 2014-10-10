%define upstream_name    Config-Model-Itself
%define upstream_version 1.238

Name:		perl-%{upstream_name}
Version:	%perl_convert_version %{upstream_version}
Release:	2

Summary:	Edit and validate configuration models
License:	GPL+ or Artistic
Group:		Development/Perl
Url:		http://search.cpan.org/dist/%{upstream_name}
Source0:	http://www.cpan.org/modules/by-module/Config/Config-Model-Itself-%{upstream_version}.tar.gz

BuildRequires:	perl-devel
BuildRequires: perl(namespace::autoclean)
BuildRequires:	perl(Config::Model::TkUI)
BuildRequires:	perl(Config::Model)
BuildRequires:	perl(Exception::Class)
BuildRequires:	perl(Module::Build)
BuildRequires:	perl(Pod::POM)
BuildRequires:	x11-server-xvfb

BuildArch:	noarch

%description
The Config::Itself and its model files provide a model of Config:Model
(hence the Itself name).

Let's step back a little to explain. Any configuration data is, in essence,
structured data. This data could be stored in an XML file. A configuration
model is a way to describe the structure and relation of all items of a
configuration data set.

This configuration model is also expressed as structured data. This
structure data is structured and follow a set of rules which are described
for humans in the Config::Model manpage.

%prep
%setup -q -n %{upstream_name}-%{upstream_version} 

%build
perl Build.PL installdirs=vendor
./Build

#%check
#xvfb-run -n 14 
#./Build test

%install
./Build install destdir=%{buildroot}

%files
%doc README 
%{_mandir}/man1/*
%{_mandir}/man3/*
%{_bindir}/config-model-edit
%{perl_vendorlib}/Config

%changelog
* Wed Jun 22 2011 Guillaume Rousse <guillomovitch@mandriva.org> 1.225.0-1mdv2011.0
+ Revision: 686619
- update to new version 1.225

* Sun Apr 10 2011 Bruno Cornec <bcornec@mandriva.org> 1.224.0-1
+ Revision: 652163
- Update Config-Model-Itself to 1.224 upstream

  + Guillaume Rousse <guillomovitch@mandriva.org>
    - update to new version 1.223

* Tue Mar 08 2011 Sandro Cazzaniga <kharec@mandriva.org> 1.222.0-1
+ Revision: 642877
- new version
- drop %%check
- add a BR on Config::Model

* Mon Nov 08 2010 Guillaume Rousse <guillomovitch@mandriva.org> 1.219.0-1mdv2011.0
+ Revision: 595086
- update to new version 1.219

* Mon Aug 16 2010 Jérôme Quelin <jquelin@mandriva.org> 1.216.0-1mdv2011.0
+ Revision: 570570
- using display 14 for xvfb-run (99 is too often busy)
- update to 1.216

* Wed Apr 07 2010 Jérôme Quelin <jquelin@mandriva.org> 1.215.0-1mdv2010.1
+ Revision: 532711
- update to 1.215

* Thu Apr 01 2010 Jérôme Quelin <jquelin@mandriva.org> 1.214.0-1mdv2010.1
+ Revision: 530665
- update to 1.214

* Tue Mar 30 2010 Jérôme Quelin <jquelin@mandriva.org> 1.213.0-1mdv2010.1
+ Revision: 529818
- adding missing buildrequires:
- update to 1.213

* Sun Feb 28 2010 Jérôme Quelin <jquelin@mandriva.org> 1.212.0-1mdv2010.1
+ Revision: 512599
- update to 1.212

* Tue Jul 07 2009 Guillaume Rousse <guillomovitch@mandriva.org> 1.211.0-1mdv2010.0
+ Revision: 393074
- import perl-Config-Model-Itself


* Mon Jul 06 2009 cpan2dist 1.211-1mdv
- initial mdv release, generated with cpan2dist



