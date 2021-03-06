Name:           altprobe
Version:        1.0
Release:        1%{?dist}
Summary:        Alertflex collector

License:        Apache License 2.0
# URL:
# Source0:        altprobe-1.0.tar.gz
BuildArch:      x86_64

BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)

# BuildRequires:
# Requires:

%description
Alertflex collector

# %prep
%setup -q


# %build
#%configure
#make %{?_smp_mflags}


%install
rm -rf $RPM_BUILD_ROOT
install -d -m 0755 $RPM_BUILD_ROOT/etc/altprobe
install -m 0755 $RPM_SOURCE_DIR/altprobe.yaml $RPM_BUILD_ROOT/etc/altprobe/altprobe.yaml
install -m 0755 $RPM_SOURCE_DIR/filters.json $RPM_BUILD_ROOT/etc/altprobe/filters.json
install -d -m 0755 $RPM_BUILD_ROOT/etc/altprobe/scripts
install -m 0755 $RPM_SOURCE_DIR/scripts/iprepup-suri.sh $RPM_BUILD_ROOT/etc/altprobe/scripts/iprepup-suri.sh
install -m 0755 $RPM_SOURCE_DIR/scripts/iprepup-wazuh.sh $RPM_BUILD_ROOT/etc/altprobe/scripts/iprepup-wazuh.sh
install -m 0755 $RPM_SOURCE_DIR/scripts/restart-falco.sh $RPM_BUILD_ROOT/etc/altprobe/scripts/restart-falco.sh
install -m 0755 $RPM_SOURCE_DIR/scripts/restart-suri.sh $RPM_BUILD_ROOT/etc/altprobe/scripts/restart-suri.sh
install -m 0755 $RPM_SOURCE_DIR/scripts/restart-wazuh.sh $RPM_BUILD_ROOT/etc/altprobe/scripts/restart-wazuh.sh
install -m 0755 $RPM_SOURCE_DIR/scripts/rulesup-falco.sh $RPM_BUILD_ROOT/etc/altprobe/scripts/rulesup-falco.sh
install -m 0755 $RPM_SOURCE_DIR/scripts/rulesup-suri.sh $RPM_BUILD_ROOT/etc/altprobe/scripts/rulesup-suri.sh
install -m 0755 $RPM_SOURCE_DIR/scripts/rulesup-wazuh.sh $RPM_BUILD_ROOT/etc/altprobe/scripts/rulesup-wazuh.sh
install -d -m 0755 $RPM_BUILD_ROOT/usr/sbin
install -m 0755 $RPM_SOURCE_DIR/altprobe $RPM_BUILD_ROOT/usr/sbin/altprobe
install -m 0755 $RPM_SOURCE_DIR/scripts/altprobe-restart $RPM_BUILD_ROOT/usr/sbin/altprobe-restart
install -m 0755 $RPM_SOURCE_DIR/scripts/altprobe-start $RPM_BUILD_ROOT/usr/sbin/altprobe-start
install -m 0755 $RPM_SOURCE_DIR/scripts/altprobe-status $RPM_BUILD_ROOT/usr/sbin/altprobe-status
install -m 0755 $RPM_SOURCE_DIR/scripts/altprobe-stop $RPM_BUILD_ROOT/usr/sbin/altprobe-stop


%files

%defattr(-,root,root,-)

/etc/altprobe/altprobe.yaml
/etc/altprobe/filters.json
/etc/altprobe/scripts/iprepup-suri.sh
/etc/altprobe/scripts/iprepup-wazuh.sh
/etc/altprobe/scripts/restart-falco.sh
/etc/altprobe/scripts/restart-suri.sh
/etc/altprobe/scripts/restart-wazuh.sh
/etc/altprobe/scripts/rulesup-falco.sh
/etc/altprobe/scripts/rulesup-suri.sh
/etc/altprobe/scripts/rulesup-wazuh.sh
/usr/sbin/altprobe
/usr/sbin/altprobe-restart
/usr/sbin/altprobe-start
/usr/sbin/altprobe-status
/usr/sbin/altprobe-stop

%changelog
