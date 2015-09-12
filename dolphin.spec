
# Please do not update/rebuild/touch this package before asking first to mikala and/or neoclust
# This package is part of the KDE Stack.
#
#define debug_package %{nil}

%define rel 1

Summary:        File manager for KDE focusing on usability
Name:           dolphin
Version: 15.08.0
Epoch:          1
Release:        %mkrel %rel
License:        GPLv2+
Group:          System/Base
Source0:        http://fr2.rpmfind.net/linux/KDE/stable/plasma/%{name}-%{version}.tar.xz
URL:            https://www.kde.org/

BuildRequires:  pkgconfig(Qt5Core)
BuildRequires:  pkgconfig(Qt5Concurrent)
BuildRequires:  pkgconfig(Qt5Widgets)
BuildRequires:  pkgconfig(Qt5Gui)
BuildRequires:  pkgconfig(Qt5DBus)
BuildRequires:  pkgconfig(Qt5Test)

BuildRequires:  kf5-macros
BuildRequires:  kactivities-devel >= 5.7.0
BuildRequires:  baloo-devel >= 4.97
BuildRequires:  kfilemetadata-devel >= 4.97
BuildRequires:  kdoctools-devel >= 5.7.0
BuildRequires:  kinit-devel >= 5.7.0
BuildRequires:  kcmutils-devel >= 5.7.0
BuildRequires:  knewstuff-devel >= 5.7.0
BuildRequires:  kcoreaddons-devel >= 5.7.0
BuildRequires:  ki18n-devel >= 5.7.0
BuildRequires:  kdbusaddons-devel >= 5.7.0
BuildRequires:  kbookmarks-devel >= 5.7.0
BuildRequires:  kconfig-devel >= 5.7.0
BuildRequires:  kio-devel >= 5.7.0
BuildRequires:  solid-devel >= 5.7.0
BuildRequires:  kiconthemes-devel >= 5.7.0
BuildRequires:  kcompletion-devel >= 5.7.0
BuildRequires:  kparts >= 5.12.0
BuildRequires:  ktexteditor-devel >= 5.7.0
BuildRequires:  kwindowsystem-devel >= 5.7.0
BuildRequires:  knotifications-devel >= 5.7.0
BuildRequires:  phonon4qt5-devel
BuildRequires:  kdelibs4support-devel >= 5.7.0

BuildRequires:  baloo-widgets-devel >= 4.97

BuildRequires:	libxml2-utils
BuildRequires:	docbook-dtds
BuildRequires:	docbook-style-xsl

%description
Dolphin is a file manager for KDE focusing on usability.
The main features of Dolphin are:
- Navigation bar for URLs, which allows to navigate quickly
     through the file hierarchy.
- View properties are remembered for each folder.
- Split of views is supported.
- Network transparency.
- Undo/redo functionality.
- Renaming of a variable number of selected items in one step.

Dolphin is not intended to be a competitor to Konqueror: Konqueror
acts as universal viewer being able to show HTML pages, text documents,
directories and a lot more, whereas Dolphin focuses on being only a file
manager. This approach allows to optimize the user interface for the task
of file management.

%files 
%_kf5_bindir/dolphin
%_kf5_bindir/servicemenudeinstallation
%_kf5_bindir/servicemenuinstallation
%_sysconfdir/xdg/servicemenu.knsrc
%_kf5_libdir/libkdeinit5_dolphin.so
%_qt5_plugindir/*.so
%_kf5_datadir/appdata/dolphin.appdata.xml
%_kf5_datadir/applications/org.kde.dolphin.desktop
%_kf5_datadir/config.kcfg/*.kcfg
%_datadir/dbus-1/interfaces/org.freedesktop.FileManager1.xml
%_datadir/dbus-1/services/org.kde.dolphin.FileManager1.service
%_kf5_services/*.desktop
%_kf5_servicetypes/fileviewversioncontrolplugin.desktop
%_kf5_datadir/kxmlgui5/dolphin
%_kf5_datadir/kxmlgui5/dolphinpart

#--------------------------------------------------------------------

%package handbook
Summary: %{name} Handbook
BuildArch: noarch

%description handbook
This package provides %{name} Handbook.

%files handbook
%doc %_docdir/HTML/*/dolphin

#--------------------------------------------------------------------

%define dolphinprivate_major 15
%define libdolphinprivate %mklibname dolphinprivate %{dolphinprivate_major}

%package -n %libdolphinprivate
Summary:      Widgets for Baloo
Group:        System/Libraries

%description -n %libdolphinprivate
Dolphin Library

%files -n %libdolphinprivate
%_kf5_libdir/libdolphinprivate.so.%{dolphinprivate_major}*
%_kf5_libdir/libdolphinprivate.so.5

#--------------------------------------------------------------------

%define dolphinvcs_major 15
%define libdolphinvcs %mklibname dolphinvcs %{dolphinvcs_major}

%package -n %libdolphinvcs
Summary:      Widgets for Baloo
Group:        System/Libraries


%description -n %libdolphinvcs
Dolphin Library

%files -n %libdolphinvcs
%_kf5_libdir/libdolphinvcs.so.%{dolphinvcs_major}*
%_kf5_libdir/libdolphinvcs.so.5

#--------------------------------------------------------------------

%define dolphin_devel %mklibname dolphin -d

%package -n %dolphin_devel

Summary:        Devel stuff for %name
Group:          Development/KDE and Qt
Requires:       %name = %epoch:%version-%release
Requires:       %libdolphinprivate = %epoch:%version-%release
Requires:       %libdolphinvcs = %epoch:%version-%release
Provides:       %name-devel = %epoch:%{version}-%{release}



%description -n %dolphin_devel
This package contains header files needed if you wish to build applications
based on %name.

%files -n %dolphin_devel
%_includedir/Dolphin
%_includedir/dolphin_export.h
%_libdir/cmake/DolphinVcs
%_kf5_libdir/*.so

#--------------------------------------------------------------------

%prep
%setup -q 
%apply_patches

%build
%cmake_kf5 -DSYSCONF_INSTALL_DIR="%_sysconfdir"
%make

%install
%makeinstall_std -C build



%changelog
* Wed Aug 19 2015 neoclust <neoclust> 1:15.08.0-1.mga6
+ Revision: 865905
- New version 15.08.0

* Wed Aug 12 2015 neoclust <neoclust> 1:15.07.90-2.mga6
+ Revision: 863900
- Plasma Mass Rebuild - Rebuild for new Plasma

* Sun Aug 09 2015 neoclust <neoclust> 1:15.07.90-1.mga6
+ Revision: 862058
- Remove empty dolphin.lang
- New version 15.07.90

* Wed Jul 29 2015 neoclust <neoclust> 1:15.07.80-1.mga6
+ Revision: 858787
- imported package dolphin

