Name:           ros-hydro-navigation
Version:        1.11.16
Release:        0%{?dist}
Summary:        ROS navigation package

Group:          Development/Libraries
License:        BSD,LGPL,LGPL (amcl)
URL:            http://wiki.ros.org/navigation
Source0:        %{name}-%{version}.tar.gz

BuildArch:      noarch

Requires:       ros-hydro-amcl
Requires:       ros-hydro-base-local-planner
Requires:       ros-hydro-carrot-planner
Requires:       ros-hydro-clear-costmap-recovery
Requires:       ros-hydro-costmap-2d
Requires:       ros-hydro-dwa-local-planner
Requires:       ros-hydro-fake-localization
Requires:       ros-hydro-global-planner
Requires:       ros-hydro-map-server
Requires:       ros-hydro-move-base
Requires:       ros-hydro-move-base-msgs
Requires:       ros-hydro-move-slow-and-clear
Requires:       ros-hydro-nav-core
Requires:       ros-hydro-navfn
Requires:       ros-hydro-robot-pose-ekf
Requires:       ros-hydro-rotate-recovery
Requires:       ros-hydro-voxel-grid
BuildRequires:  ros-hydro-catkin

%description
A 2D navigation stack that takes in information from odometry, sensor streams,
and a goal pose and outputs safe velocity commands that are sent to a mobile
base.

%prep
%setup -q

%build
# In case we're installing to a non-standard location, look for a setup.sh
# in the install tree that was dropped by catkin, and source it.  It will
# set things like CMAKE_PREFIX_PATH, PKG_CONFIG_PATH, and PYTHONPATH.
if [ -f "/opt/ros/hydro/setup.sh" ]; then . "/opt/ros/hydro/setup.sh"; fi
mkdir -p obj-%{_target_platform} && cd obj-%{_target_platform}
%cmake .. \
        -UINCLUDE_INSTALL_DIR \
        -ULIB_INSTALL_DIR \
        -USYSCONF_INSTALL_DIR \
        -USHARE_INSTALL_PREFIX \
        -ULIB_SUFFIX \
        -DCMAKE_INSTALL_PREFIX="/opt/ros/hydro" \
        -DCMAKE_PREFIX_PATH="/opt/ros/hydro" \
        -DSETUPTOOLS_DEB_LAYOUT=OFF \
        -DCATKIN_BUILD_BINARY_PACKAGE="1" \

make %{?_smp_mflags}

%install
# In case we're installing to a non-standard location, look for a setup.sh
# in the install tree that was dropped by catkin, and source it.  It will
# set things like CMAKE_PREFIX_PATH, PKG_CONFIG_PATH, and PYTHONPATH.
if [ -f "/opt/ros/hydro/setup.sh" ]; then . "/opt/ros/hydro/setup.sh"; fi
cd obj-%{_target_platform}
make %{?_smp_mflags} install DESTDIR=%{buildroot}

%files
/opt/ros/hydro

%changelog
* Thu Apr 30 2015 David V. Lu!! <davidvlu@gmail.com> - 1.11.16-0
- Autogenerated by Bloom

* Tue Feb 03 2015 David V. Lu!! <davidvlu@gmail.com> - 1.11.15-0
- Autogenerated by Bloom

* Fri Dec 05 2014 David V. Lu!! <davidvlu@gmail.com> - 1.11.14-0
- Autogenerated by Bloom

* Thu Oct 02 2014 David V. Lu!! <davidvlu@gmail.com> - 1.11.13-0
- Autogenerated by Bloom

* Wed Oct 01 2014 David V. Lu!! <davidvlu@gmail.com> - 1.11.12-0
- Autogenerated by Bloom

