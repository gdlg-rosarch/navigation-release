Name:           ros-jade-nav-core
Version:        1.13.1
Release:        0%{?dist}
Summary:        ROS nav_core package

Group:          Development/Libraries
License:        BSD
URL:            http://wiki.ros.org/nav_core
Source0:        %{name}-%{version}.tar.gz

Requires:       ros-jade-costmap-2d
Requires:       ros-jade-geometry-msgs
Requires:       ros-jade-std-msgs
Requires:       ros-jade-tf
BuildRequires:  ros-jade-catkin
BuildRequires:  ros-jade-costmap-2d
BuildRequires:  ros-jade-geometry-msgs
BuildRequires:  ros-jade-std-msgs
BuildRequires:  ros-jade-tf

%description
This package provides common interfaces for navigation specific robot actions.
Currently, this package provides the BaseGlobalPlanner, BaseLocalPlanner, and
RecoveryBehavior interfaces, which can be used to build actions that can easily
swap their planner, local controller, or recovery behavior for new versions
adhering to the same interface.

%prep
%setup -q

%build
# In case we're installing to a non-standard location, look for a setup.sh
# in the install tree that was dropped by catkin, and source it.  It will
# set things like CMAKE_PREFIX_PATH, PKG_CONFIG_PATH, and PYTHONPATH.
if [ -f "/opt/ros/jade/setup.sh" ]; then . "/opt/ros/jade/setup.sh"; fi
mkdir -p obj-%{_target_platform} && cd obj-%{_target_platform}
%cmake .. \
        -UINCLUDE_INSTALL_DIR \
        -ULIB_INSTALL_DIR \
        -USYSCONF_INSTALL_DIR \
        -USHARE_INSTALL_PREFIX \
        -ULIB_SUFFIX \
        -DCMAKE_INSTALL_PREFIX="/opt/ros/jade" \
        -DCMAKE_PREFIX_PATH="/opt/ros/jade" \
        -DSETUPTOOLS_DEB_LAYOUT=OFF \
        -DCATKIN_BUILD_BINARY_PACKAGE="1" \

make %{?_smp_mflags}

%install
# In case we're installing to a non-standard location, look for a setup.sh
# in the install tree that was dropped by catkin, and source it.  It will
# set things like CMAKE_PREFIX_PATH, PKG_CONFIG_PATH, and PYTHONPATH.
if [ -f "/opt/ros/jade/setup.sh" ]; then . "/opt/ros/jade/setup.sh"; fi
cd obj-%{_target_platform}
make %{?_smp_mflags} install DESTDIR=%{buildroot}

%files
/opt/ros/jade

%changelog
* Fri Oct 30 2015 David V. Lu!! <davidvlu@gmail.com> - 1.13.1-0
- Autogenerated by Bloom

* Tue Mar 17 2015 David V. Lu!! <davidvlu@gmail.com> - 1.13.0-0
- Autogenerated by Bloom

