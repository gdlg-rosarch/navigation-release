Name:           ros-lunar-carrot-planner
Version:        1.15.2
Release:        0%{?dist}
Summary:        ROS carrot_planner package

Group:          Development/Libraries
License:        BSD
URL:            http://wiki.ros.org/carrot_planner
Source0:        %{name}-%{version}.tar.gz

Requires:       eigen3-devel
Requires:       ros-lunar-base-local-planner
Requires:       ros-lunar-costmap-2d
Requires:       ros-lunar-nav-core
Requires:       ros-lunar-pluginlib
Requires:       ros-lunar-roscpp
Requires:       ros-lunar-tf
BuildRequires:  eigen3-devel
BuildRequires:  ros-lunar-base-local-planner
BuildRequires:  ros-lunar-catkin
BuildRequires:  ros-lunar-costmap-2d
BuildRequires:  ros-lunar-nav-core
BuildRequires:  ros-lunar-pluginlib
BuildRequires:  ros-lunar-roscpp
BuildRequires:  ros-lunar-tf

%description
This planner attempts to find a legal place to put a carrot for the robot to
follow. It does this by moving back along the vector between the robot and the
goal point.

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

