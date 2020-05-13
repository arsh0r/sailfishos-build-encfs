#
# spec file for package encfs
#
# Copyright (c) 2020 SUSE LLC
#
# All modifications and additions to the file contributed by third parties
# remain the property of their copyright owners, unless otherwise agreed
# upon. The license for this file, and modifications and additions to the
# file, is the same license as for the pristine package itself (unless the
# license for the pristine package is not an Open Source License, in which
# case the license is the MIT License). An "Open Source License" is a
# license that conforms to the Open Source Definition (Version 1.9)
# published by the Open Source Initiative.

# Please submit bugfixes or comments via https://bugs.opensuse.org/
#

Name:           encfs
Version:        1.9.5
Release:        1
Summary:        Userspace Encrypted File System
License:        GPL-2.0-or-later AND GPL-3.0-or-later
Group:          System/Filesystems
URL:            https://vgough.github.io/encfs/
Source:         https://github.com/vgough/encfs/releases/download/v%{version}/encfs-%{version}.tar.gz
Prefix:         /usr
Provides:       encfs
Provides:       encfsctl
BuildRequires:  cmake >= 3.0.2
BuildRequires:  fuse-devel
BuildRequires:  gcc-c++
BuildRequires:  openssl-devel
BuildRequires:  pkgconfig
Requires:       fuse
BuildRoot:      %{_tmppath}/%{name}-%{version}-build

%description
EncFS provides an encrypted file system, layered on top of a normal
directory tree and encrypts individual files which are stored in the
hosting directory tree.

This has several advantages over the loopback encryption which
provided by the Linux kernel: 
- No space is and has to be reserved, encrypted files only 
  take the space that they really occupy
- Backups: encrypted files can be individually backed-up on the host
  filesystem
- Layering: Since it's hosted on a normal filesystem, encfs can be
  used on filesystems which normally have no support encryption,
  like NFS or other userspace filesystems.

EncFS is implemented as a userspace filesystem in an unprivileged
application using fuse (FUSE (Filesystem in USErspace)).


%prep
rm -rf $RPM_BUILD_ROOT 
mkdir $RPM_BUILD_ROOT
%setup 

%build
mkdir -p build
cd build
/usr/bin/cmake -DBUILD_UNIT_TESTS=OFF -DENABLE_NLS=OFF -DCMAKE_INSTALL_PREFIX=%{_prefix} ..
make VERBOSE=1

%install
cd build
make DESTDIR=$RPM_BUILD_ROOT install
chmod 755 "%{buildroot}%{_bindir}/encfssh"


%files 
%defattr(-,root,root)
%{_bindir}/encfs*

%defattr(-,root,root)

%changelog
