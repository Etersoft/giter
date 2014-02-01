Name: giter
Version: 0.1
Release: alt1

Summary: Etersoft wrapper for git commands

License: AGPLv3
Group: Development/Other
Url: http://wiki.etersoft.ru/Giter

Packager: Vitaly Lipatov <lav@altlinux.ru>

# git-clone http://git.altlinux.org/people/lav/packages/giter.git
Source: ftp://updates.etersoft.ru/pub/Etersoft/Sisyphus/sources/tarball/%name-%version.tar

BuildArchitectures: noarch

%description
This package contains a set of helper utils for git and gitum.
See info in Russian on %url.

RECOMMENDED packages: git-core gitum

%prep
%setup

#build
#make

%install
# install to datadir and so on
%makeinstall
%find_lang %name

%files -f %name.lang
%doc AUTHORS
%_bindir/*

%changelog
* Thu Jan 30 2014 Vitaly Lipatov <lav@altlinux.ru> 0.1-alt1
- initial build for ALT Linux Sisyphus