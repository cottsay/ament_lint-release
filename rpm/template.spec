%bcond_without tests
%bcond_without weak_deps

%global __os_install_post %(echo '%{__os_install_post}' | sed -e 's!/usr/lib[^[:space:]]*/brp-python-bytecompile[[:space:]].*$!!g')
%global __provides_exclude_from ^/opt/ros/eloquent/.*$
%global __requires_exclude_from ^/opt/ros/eloquent/.*$

Name:           ros-eloquent-ament-cpplint
Version:        0.8.1
Release:        2%{?dist}%{?release_suffix}
Summary:        ROS ament_cpplint package

License:        Apache License 2.0
Source0:        %{name}-%{version}.tar.gz

Requires:       ros-eloquent-ros-workspace
BuildRequires:  python%{python3_pkgversion}-devel
BuildRequires:  python3-pytest
BuildRequires:  ros-eloquent-ament-copyright
BuildRequires:  ros-eloquent-ament-flake8
BuildRequires:  ros-eloquent-ament-pep257
BuildRequires:  ros-eloquent-ros-workspace
Provides:       %{name}-devel = %{version}-%{release}
Provides:       %{name}-doc = %{version}-%{release}
Provides:       %{name}-runtime = %{version}-%{release}

%description
The ability to check code against the Google style conventions using cpplint and
generate xUnit test result files.

%prep
%autosetup

%build
# In case we're installing to a non-standard location, look for a setup.sh
# in the install tree and source it.  It will set things like
# CMAKE_PREFIX_PATH, PKG_CONFIG_PATH, and PYTHONPATH.
if [ -f "/opt/ros/eloquent/setup.sh" ]; then . "/opt/ros/eloquent/setup.sh"; fi
%py3_build

%install
# In case we're installing to a non-standard location, look for a setup.sh
# in the install tree and source it.  It will set things like
# CMAKE_PREFIX_PATH, PKG_CONFIG_PATH, and PYTHONPATH.
if [ -f "/opt/ros/eloquent/setup.sh" ]; then . "/opt/ros/eloquent/setup.sh"; fi
%py3_install -- --prefix "/opt/ros/eloquent"

%if 0%{?with_tests}
%check
# Look for a directory with a name indicating that it contains tests
TEST_TARGET=$(ls -d * | grep -m1 "\(test\|tests\)" ||:)
if [ -n "$TEST_TARGET" ] && %__python3 -m pytest --version; then
# In case we're installing to a non-standard location, look for a setup.sh
# in the install tree and source it.  It will set things like
# CMAKE_PREFIX_PATH, PKG_CONFIG_PATH, and PYTHONPATH.
if [ -f "/opt/ros/eloquent/setup.sh" ]; then . "/opt/ros/eloquent/setup.sh"; fi
%__python3 -m pytest $TEST_TARGET || echo "RPM TESTS FAILED"
else echo "RPM TESTS SKIPPED"; fi
%endif

%files
/opt/ros/eloquent

%changelog
* Fri Sep 18 2020 Dirk Thomas <dthomas@osrfoundation.org> - 0.8.1-2
- Autogenerated by Bloom

