%{!?directory:%define directory /usr}

%define buildroot %{_tmppath}/%{name}

Name:          pgintcl
Summary:       Pure-Tcl Interface to PostgreSQL
Version:       3.5.1
Release:       0
License:       BSD
Group:         Development/Libraries/Tcl
Source:        %{name}-%{version}.tgz
URL:           https://sourceforge.net/projects/pgintcl/
BuildArch:     noarch
BuildRequires: tcl >= 8.5
Requires:      tcl >= 8.5
BuildRoot:     %{buildroot}

%description
pgintcl is a Tcl interface to the PostgreSQL database system,
written entirely in Tcl.

%prep
%setup -q -n %{name}-%{version}

%build

%install
dir=%buildroot%tcl_noarchdir/%name%version
mkdir -p $dir
cp *.tcl $dir

%clean
rm -rf %buildroot

%files
%defattr(-,root,root)
%doc COPYING INTERNALS NEWS README REFERENCE
%tcl_noarchdir/%name%version

