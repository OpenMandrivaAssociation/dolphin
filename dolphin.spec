Summary:	File manager for KDE focusing on usability
Name:		dolphin
Version:	17.04.3
Epoch:		1
Release:	1
License:	GPLv2+
Group:		Graphical desktop/KDE
%define is_beta %(if test `echo %{version} |cut -d. -f3` -ge 70; then echo -n 1; else echo -n 0; fi)
%if %{is_beta}
%define ftpdir unstable
%else
%define ftpdir stable
%endif
Source0:	http://download.kde.org/%{ftpdir}/applications/%{version}/src/%{name}-%{version}.tar.xz
URL:		https://www.kde.org/
# (tpg) Patch from Rosa https://abf.rosalinux.ru/import/plasma5-dolphin/commit/8d7cd84c80ed66937f5cedcba38fd66484e68b93
Patch0:		dolphin-15.08.1-klook.patch
BuildRequires:	pkgconfig(Qt5Core)
BuildRequires:	pkgconfig(Qt5Concurrent)
BuildRequires:	pkgconfig(Qt5Widgets)
BuildRequires:	pkgconfig(Qt5Gui)
BuildRequires:	pkgconfig(Qt5DBus)
BuildRequires:	pkgconfig(Qt5Test)

BuildRequires:	cmake(ECM)
BuildRequires:	cmake(KF5DocTools)
BuildRequires:	cmake(KF5Init)
BuildRequires:	cmake(KF5KCMUtils)
BuildRequires:	cmake(KF5NewStuff)
BuildRequires:	cmake(KF5CoreAddons)
BuildRequires:	cmake(KF5I18n)
BuildRequires:	cmake(KF5DBusAddons)
BuildRequires:	cmake(KF5Bookmarks)
BuildRequires:	cmake(KF5Config)
BuildRequires:	cmake(KF5KIO)
BuildRequires:	cmake(KF5Solid)
BuildRequires:	cmake(KF5IconThemes)
BuildRequires:	cmake(KF5Completion)
BuildRequires:	cmake(KF5Parts)
BuildRequires:	cmake(KF5TextEditor)
BuildRequires:	cmake(KF5WindowSystem)
BuildRequires:	cmake(KF5Notifications)
BuildRequires:	cmake(KF5XmlGui)
BuildRequires:	cmake(KF5Attica)
BuildRequires:	cmake(Phonon4Qt5)

BuildRequires:	cmake(KF5Activities)
BuildRequires:	cmake(KF5Baloo)
BuildRequires:	cmake(KF5BalooWidgets)
BuildRequires:	cmake(KF5FileMetaData)
BuildRequires:	cmake(KF5KDELibs4Support)

BuildRequires:	libxml2-utils
BuildRequires:	docbook-dtds
BuildRequires:	docbook-style-xsl
BuildRequires:	ninja

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

%files -f %{name}.lang
%_kde5_bindir/dolphin
%_kde5_bindir/servicemenudeinstallation
%_kde5_bindir/servicemenuinstallation
%_sysconfdir/xdg/servicemenu.knsrc
%_kde5_libdir/libkdeinit5_dolphin.so
%_qt5_plugindir/*.so
%_kde5_datadir/applications/org.kde.dolphin.desktop
%_kde5_datadir/config.kcfg/*.kcfg
%_datadir/metainfo/org.kde.dolphin.appdata.xml
%_datadir/dbus-1/interfaces/org.freedesktop.FileManager1.xml
%_datadir/dbus-1/services/org.kde.dolphin.FileManager1.service
%_kde5_services/*.desktop
%_kde5_servicetypes/fileviewversioncontrolplugin.desktop
%_kde5_datadir/kxmlgui5/dolphin
%_kde5_datadir/kxmlgui5/dolphinpart
%lang(fi) %{_datadir}/locale/fi/LC_SCRIPTS/dolphin

#--------------------------------------------------------------------

%package handbook
Summary:	%{name} Handbook
BuildArch:	noarch

%description handbook
This package provides %{name} Handbook.

%files handbook
%doc %_docdir/HTML/*/dolphin

#--------------------------------------------------------------------

%define dolphinprivate_major 5
%define libdolphinprivate %mklibname dolphinprivate %{dolphinprivate_major}

%package -n %{libdolphinprivate}
Summary:	Dolphin library
Group:		System/Libraries
Obsoletes:	%{mklibname dolphinprivate 15} < 15.12.0

%description -n %{libdolphinprivate}
Dolphin Library.

%files -n %{libdolphinprivate}
%_kde5_libdir/libdolphinprivate.so.%{dolphinprivate_major}*

#--------------------------------------------------------------------

%define dolphinvcs_major 5
%define libdolphinvcs %mklibname dolphinvcs %{dolphinvcs_major}

%package -n %{libdolphinvcs}
Summary:	Dolphin library
Group:		System/Libraries
Obsoletes:	%{mklibname dolphinvcs 15} < 15.12.0

%description -n %{libdolphinvcs}
Dolphin Library.

%files -n %{libdolphinvcs}
%_kde5_libdir/libdolphinvcs.so.%{dolphinvcs_major}*

#--------------------------------------------------------------------

%package devel
Summary:	Development stuff for %{name}
Group:		Development/KDE and Qt
Requires:	%{name} = %{EVRD}
Requires:	%{libdolphinprivate} = %{EVRD}
Requires:	%{libdolphinvcs} = %{EVRD}
Provides:	%{name}-devel = %{EVRD}
Obsoletes:	%{mklibname dolphin -d} < 15.08.2-2

%description devel
This package contains header files needed if you wish to build applications
based on %{name}.

%files devel
%exclude %_kde5_libdir/libkdeinit5_dolphin.so
%_includedir/Dolphin
%_includedir/dolphin_export.h
%_includedir/dolphinvcs_export.h
%_libdir/cmake/DolphinVcs
%_kde5_libdir/*.so

#--------------------------------------------------------------------

%prep
%setup -q
%apply_patches

%build
%cmake_kde5 -DSYSCONF_INSTALL_DIR="%{_sysconfdir}"
%ninja

%install
%ninja_install -C build
%find_lang %{name}
