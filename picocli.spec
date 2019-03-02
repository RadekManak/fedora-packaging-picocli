Name:       picocli
Version:    3.9.5
Release:    1%{?dist}
Summary:    Java command line parser with both an annotations API and a programmatic API

License:    ASL 2.0
URL:        https://github.com/remkop/%{name}
Source0:    https://github.com/remkop/%{name}/archive/v%{version}.tar.gz
Patch0:     0001-build-without-asciidoctor-bintray-and-system-rules.patch

BuildArch:      noarch
BuildRequires:  gradle-local
BuildRequires:  git
# Should be added using Xmvn
# BuildRequires:  groovy
# BuildRequires:  jline2
#Downgrade requirement to packaged version
BuildRequires:  jline3

%description
Picocli is a one-file framework for creating Java command line applications
with almost zero code. Supports a variety of command line syntax styles
including POSIX, GNU, MS-DOS and more. Generates highly customizable usage
help messages with ANSI colors and styles.

%prep
%autosetup -S git

%build
%gradle_build -f

%install
%mvn_install

%files -f .mfiles

%license LICENSE

%changelog
* Sat Mar 02 2019 Radek Maňák <Radek.Manak@protonmail.com> 3.9.5-1
- initial package
