Name:           oomd5
Version:        0.1.0
Release:        1%{?dist}
Summary:        Legacy MD5 hash calculator for verifying legacy file distribution manifests.
License:        ASL 2.0
URL:            https://github.com/openOODA-tools/oomd5
Source0:        oomd5-linux-x86_64
Source1:        uninstall.sh
BuildArch:      x86_64
Requires:       glibc

%description
oomd5 is a sovereign, capability-bounded MD5 LEGACY written
in pure openOODA, featuring zero ambient authority, oote color themes,
and an MCP stdio server.

%install
mkdir -p %{buildroot}/usr/bin
install -m 0755 %{SOURCE0} %{buildroot}/usr/bin/oomd5
install -m 0755 %{SOURCE1} %{buildroot}/usr/bin/oomd5-uninstall

%files
/usr/bin/oomd5
/usr/bin/oomd5-uninstall

%changelog
* Wed Oct 07 2026 openOODA-tools <ops@openooda.org> - 0.1.0-1
- Initial sovereign blueprint scaffolding
