Name:           ros-indigo-move-base
Version:        1.12.6
Release:        0%{?dist}
Summary:        ROS move_base package

Group:          Development/Libraries
License:        BSD
URL:            http://wiki.ros.org/move_base
Source0:        %{name}-%{version}.tar.gz

Requires:       ros-indigo-actionlib
Requires:       ros-indigo-base-local-planner
Requires:       ros-indigo-clear-costmap-recovery
Requires:       ros-indigo-costmap-2d
Requires:       ros-indigo-dynamic-reconfigure
Requires:       ros-indigo-geometry-msgs
Requires:       ros-indigo-message-runtime
Requires:       ros-indigo-move-base-msgs
Requires:       ros-indigo-nav-core
Requires:       ros-indigo-nav-msgs
Requires:       ros-indigo-navfn
Requires:       ros-indigo-pluginlib
Requires:       ros-indigo-roscpp
Requires:       ros-indigo-rospy
Requires:       ros-indigo-rotate-recovery
Requires:       ros-indigo-std-msgs
Requires:       ros-indigo-std-srvs
Requires:       ros-indigo-tf
Requires:       ros-indigo-visualization-msgs
BuildRequires:  ros-indigo-actionlib
BuildRequires:  ros-indigo-base-local-planner
BuildRequires:  ros-indigo-catkin
BuildRequires:  ros-indigo-clear-costmap-recovery
BuildRequires:  ros-indigo-cmake-modules
BuildRequires:  ros-indigo-costmap-2d
BuildRequires:  ros-indigo-dynamic-reconfigure
BuildRequires:  ros-indigo-geometry-msgs
BuildRequires:  ros-indigo-message-generation
BuildRequires:  ros-indigo-move-base-msgs
BuildRequires:  ros-indigo-nav-core
BuildRequires:  ros-indigo-nav-msgs
BuildRequires:  ros-indigo-navfn
BuildRequires:  ros-indigo-pluginlib
BuildRequires:  ros-indigo-roscpp
BuildRequires:  ros-indigo-rospy
BuildRequires:  ros-indigo-rotate-recovery
BuildRequires:  ros-indigo-std-msgs
BuildRequires:  ros-indigo-std-srvs
BuildRequires:  ros-indigo-tf
BuildRequires:  ros-indigo-visualization-msgs

%description
The move_base package provides an implementation of an action (see the actionlib
package) that, given a goal in the world, will attempt to reach it with a mobile
base. The move_base node links together a global and local planner to accomplish
its global navigation task. It supports any global planner adhering to the
nav_core::BaseGlobalPlanner interface specified in the nav_core package and any
local planner adhering to the nav_core::BaseLocalPlanner interface specified in
the nav_core package. The move_base node also maintains two costmaps, one for
the global planner, and one for a local planner (see the costmap_2d package)
that are used to accomplish navigation tasks.

%prep
%setup -q

%build
# In case we're installing to a non-standard location, look for a setup.sh
# in the install tree that was dropped by catkin, and source it.  It will
# set things like CMAKE_PREFIX_PATH, PKG_CONFIG_PATH, and PYTHONPATH.
if [ -f "/opt/ros/indigo/setup.sh" ]; then . "/opt/ros/indigo/setup.sh"; fi
mkdir -p obj-%{_target_platform} && cd obj-%{_target_platform}
%cmake .. \
        -UINCLUDE_INSTALL_DIR \
        -ULIB_INSTALL_DIR \
        -USYSCONF_INSTALL_DIR \
        -USHARE_INSTALL_PREFIX \
        -ULIB_SUFFIX \
        -DCMAKE_INSTALL_PREFIX="/opt/ros/indigo" \
        -DCMAKE_PREFIX_PATH="/opt/ros/indigo" \
        -DSETUPTOOLS_DEB_LAYOUT=OFF \
        -DCATKIN_BUILD_BINARY_PACKAGE="1" \

make %{?_smp_mflags}

%install
# In case we're installing to a non-standard location, look for a setup.sh
# in the install tree that was dropped by catkin, and source it.  It will
# set things like CMAKE_PREFIX_PATH, PKG_CONFIG_PATH, and PYTHONPATH.
if [ -f "/opt/ros/indigo/setup.sh" ]; then . "/opt/ros/indigo/setup.sh"; fi
cd obj-%{_target_platform}
make %{?_smp_mflags} install DESTDIR=%{buildroot}

%files
/opt/ros/indigo

%changelog
* Sat Jan 02 2016 David V. Lu!! <davidvlu@gmail.com> - 1.12.6-0
- Autogenerated by Bloom

* Fri Oct 30 2015 David V. Lu!! <davidvlu@gmail.com> - 1.12.5-0
- Autogenerated by Bloom

* Wed Jun 03 2015 David V. Lu!! <davidvlu@gmail.com> - 1.12.4-0
- Autogenerated by Bloom

* Thu Apr 30 2015 David V. Lu!! <davidvlu@gmail.com> - 1.12.3-0
- Autogenerated by Bloom

* Tue Mar 31 2015 David V. Lu!! <davidvlu@gmail.com> - 1.12.2-0
- Autogenerated by Bloom

* Sat Mar 14 2015 David V. Lu!! <davidvlu@gmail.com> - 1.12.1-0
- Autogenerated by Bloom

* Wed Feb 04 2015 David V. Lu!! <davidvlu@gmail.com> - 1.12.0-0
- Autogenerated by Bloom

