Name:           ros-hydro-robot-pose-ekf
Version:        1.11.16
Release:        0%{?dist}
Summary:        ROS robot_pose_ekf package

Group:          Development/Libraries
License:        BSD
URL:            http://wiki.ros.org/robot_pose_ekf
Source0:        %{name}-%{version}.tar.gz

Requires:       ros-hydro-bfl
Requires:       ros-hydro-geometry-msgs
Requires:       ros-hydro-nav-msgs
Requires:       ros-hydro-roscpp
Requires:       ros-hydro-rostest
Requires:       ros-hydro-sensor-msgs
Requires:       ros-hydro-std-msgs
Requires:       ros-hydro-tf
BuildRequires:  ros-hydro-bfl
BuildRequires:  ros-hydro-catkin >= 0.5.68
BuildRequires:  ros-hydro-geometry-msgs
BuildRequires:  ros-hydro-nav-msgs
BuildRequires:  ros-hydro-rosbag
BuildRequires:  ros-hydro-roscpp
BuildRequires:  ros-hydro-rostest
BuildRequires:  ros-hydro-sensor-msgs
BuildRequires:  ros-hydro-std-msgs
BuildRequires:  ros-hydro-tf

%description
The Robot Pose EKF package is used to estimate the 3D pose of a robot, based on
(partial) pose measurements coming from different sources. It uses an extended
Kalman filter with a 6D model (3D position and 3D orientation) to combine
measurements from wheel odometry, IMU sensor and visual odometry. The basic idea
is to offer loosely coupled integration with different sensors, where sensor
signals are received as ROS messages.

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

