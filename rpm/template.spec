Name:           ros-lunar-move-slow-and-clear
Version:        1.15.2
Release:        0%{?dist}
Summary:        ROS move_slow_and_clear package

Group:          Development/Libraries
License:        BSD
URL:            http://wiki.ros.org/move_slow_and_clear
Source0:        %{name}-%{version}.tar.gz

Requires:       ros-lunar-costmap-2d
Requires:       ros-lunar-geometry-msgs
Requires:       ros-lunar-nav-core
Requires:       ros-lunar-pluginlib
Requires:       ros-lunar-roscpp
BuildRequires:  ros-lunar-catkin
BuildRequires:  ros-lunar-cmake-modules
BuildRequires:  ros-lunar-costmap-2d
BuildRequires:  ros-lunar-geometry-msgs
BuildRequires:  ros-lunar-nav-core
BuildRequires:  ros-lunar-pluginlib
BuildRequires:  ros-lunar-roscpp

%description
move_slow_and_clear

%prep
%setup -q

%build
# In case we're installing to a non-standard location, look for a setup.sh
# in the install tree that was dropped by catkin, and source it.  It will
# set things like CMAKE_PREFIX_PATH, PKG_CONFIG_PATH, and PYTHONPATH.
if [ -f "/opt/ros/lunar/setup.sh" ]; then . "/opt/ros/lunar/setup.sh"; fi
mkdir -p obj-%{_target_platform} && cd obj-%{_target_platform}
%cmake .. \
        -UINCLUDE_INSTALL_DIR \
        -ULIB_INSTALL_DIR \
        -USYSCONF_INSTALL_DIR \
        -USHARE_INSTALL_PREFIX \
        -ULIB_SUFFIX \
        -DCMAKE_INSTALL_LIBDIR="lib" \
        -DCMAKE_INSTALL_PREFIX="/opt/ros/lunar" \
        -DCMAKE_PREFIX_PATH="/opt/ros/lunar" \
        -DSETUPTOOLS_DEB_LAYOUT=OFF \
        -DCATKIN_BUILD_BINARY_PACKAGE="1" \

make %{?_smp_mflags}

%install
# In case we're installing to a non-standard location, look for a setup.sh
# in the install tree that was dropped by catkin, and source it.  It will
# set things like CMAKE_PREFIX_PATH, PKG_CONFIG_PATH, and PYTHONPATH.
if [ -f "/opt/ros/lunar/setup.sh" ]; then . "/opt/ros/lunar/setup.sh"; fi
cd obj-%{_target_platform}
make %{?_smp_mflags} install DESTDIR=%{buildroot}

%files
/opt/ros/lunar

%changelog
* Thu Mar 22 2018 David V. Lu!! <davidvlu@gmail.com> - 1.15.2-0
- Autogenerated by Bloom

* Mon Aug 14 2017 David V. Lu!! <davidvlu@gmail.com> - 1.15.1-0
- Autogenerated by Bloom

* Mon Aug 07 2017 David V. Lu!! <davidvlu@gmail.com> - 1.15.0-0
- Autogenerated by Bloom

* Thu Jul 13 2017 David V. Lu!! <davidvlu@gmail.com> - 1.14.0-0
- Autogenerated by Bloom

