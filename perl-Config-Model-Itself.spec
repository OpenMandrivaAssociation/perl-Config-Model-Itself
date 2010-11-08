%define upstream_name    Config-Model-Itself
%define upstream_version 1.219

Name:       perl-%{upstream_name}
Version:    %perl_convert_version %{upstream_version}
Release:    %mkrel 1

Summary:    Edit and validate configuration models
License:    GPL+ or Artistic
Group:      Development/Perl
Url:        http://search.cpan.org/dist/%{upstream_name}
Source0:    http://www.cpan.org/modules/by-module/Config/%{upstream_name}-%{upstream_version}.tar.gz

BuildRequires: perl(Config::Model::TkUI)
BuildRequires: perl(Exception::Class)
BuildRequires: perl(Module::Build)
BuildRequires: perl(Pod::POM)
BuildRequires: x11-server-xvfb

BuildArch: noarch
BuildRoot:  %{_tmppath}/%{name}-%{version}

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
%{__perl} Build.PL installdirs=vendor
./Build

%check
xvfb-run -n 14 ./Build test

%install
rm -rf %buildroot
./Build install destdir=%{buildroot}

%clean
rm -rf %buildroot

%files
%defattr(-,root,root)
%doc README ChangeLog
%{_mandir}/man1/*
%{_mandir}/man3/*
%{_bindir}/config-model-edit
%{perl_vendorlib}/Config
