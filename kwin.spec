#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : kwin
Version  : 5.13.4
Release  : 3
URL      : https://github.com/KDE/kwin/archive/v5.13.4.tar.gz
Source0  : https://github.com/KDE/kwin/archive/v5.13.4.tar.gz
Summary  : No detailed summary available
Group    : Development/Tools
License  : BSD-3-Clause GFDL-1.2 GPL-2.0
Requires: kwin-bin
Requires: kwin-lib
Requires: kwin-data
Requires: kwin-license
BuildRequires : attica-dev
BuildRequires : buildreq-cmake
BuildRequires : buildreq-kde
BuildRequires : freetype-dev
BuildRequires : glibc-dev
BuildRequires : kactivities-dev
BuildRequires : kcmutils-dev
BuildRequires : kcodecs-dev
BuildRequires : kcompletion-dev
BuildRequires : kconfigwidgets-dev
BuildRequires : kcrash-dev
BuildRequires : kdeclarative-dev
BuildRequires : kdecoration-dev
BuildRequires : kglobalaccel-dev
BuildRequires : kiconthemes-dev
BuildRequires : kidletime-dev
BuildRequires : kinit-dev
BuildRequires : kio-dev
BuildRequires : kitemviews-dev
BuildRequires : kjobwidgets-dev
BuildRequires : knewstuff-dev
BuildRequires : knotifications-dev
BuildRequires : kpackage-dev
BuildRequires : kscreenlocker-dev
BuildRequires : ktextwidgets-dev
BuildRequires : kwayland-dev
BuildRequires : kwidgetsaddons-dev
BuildRequires : kwindowsystem-dev
BuildRequires : kxmlgui-dev
BuildRequires : libICE-dev
BuildRequires : libSM-dev
BuildRequires : libX11-dev libICE-dev libSM-dev libXau-dev libXcomposite-dev libXcursor-dev libXdamage-dev libXdmcp-dev libXext-dev libXfixes-dev libXft-dev libXi-dev libXinerama-dev libXi-dev libXmu-dev libXpm-dev libXrandr-dev libXrender-dev libXres-dev libXScrnSaver-dev libXt-dev libXtst-dev libXv-dev libXxf86misc-dev libXxf86vm-dev
BuildRequires : libcap-dev
BuildRequires : libepoxy-dev
BuildRequires : libinput-dev
BuildRequires : libxkbcommon-dev
BuildRequires : pkg-config
BuildRequires : pkgconfig(Qt5Gui)
BuildRequires : pkgconfig(epoxy)
BuildRequires : pkgconfig(fontconfig)
BuildRequires : pkgconfig(gbm)
BuildRequires : pkgconfig(libdrm)
BuildRequires : pkgconfig(libinput)
BuildRequires : pkgconfig(xkbcommon)
BuildRequires : plasma-framework-dev
BuildRequires : solid-dev
BuildRequires : sonnet-dev
BuildRequires : systemd-dev
BuildRequires : wayland-dev
BuildRequires : xcb-util-cursor-dev
BuildRequires : xcb-util-dev
BuildRequires : xcb-util-image-dev
BuildRequires : xcb-util-keysyms-dev
BuildRequires : xcb-util-renderutil-dev
BuildRequires : xcb-util-wm-dev
BuildRequires : xcb-util-xrm-dev

%description
- A collection of various documents and links related to KWin is at http://techbase.kde.org/Projects/KWin .

%package bin
Summary: bin components for the kwin package.
Group: Binaries
Requires: kwin-data
Requires: kwin-license

%description bin
bin components for the kwin package.


%package data
Summary: data components for the kwin package.
Group: Data

%description data
data components for the kwin package.


%package dev
Summary: dev components for the kwin package.
Group: Development
Requires: kwin-lib
Requires: kwin-bin
Requires: kwin-data
Provides: kwin-devel

%description dev
dev components for the kwin package.


%package doc
Summary: doc components for the kwin package.
Group: Documentation

%description doc
doc components for the kwin package.


%package lib
Summary: lib components for the kwin package.
Group: Libraries
Requires: kwin-data
Requires: kwin-license

%description lib
lib components for the kwin package.


%package license
Summary: license components for the kwin package.
Group: Default

%description license
license components for the kwin package.


%prep
%setup -q -n kwin-5.13.4

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C
export SOURCE_DATE_EPOCH=1535163548
mkdir clr-build
pushd clr-build
%cmake ..
make  %{?_smp_mflags}
popd

%install
export SOURCE_DATE_EPOCH=1535163548
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/doc/kwin
cp COPYING %{buildroot}/usr/share/doc/kwin/COPYING
cp COPYING.DOC %{buildroot}/usr/share/doc/kwin/COPYING.DOC
cp cmake/modules/COPYING-CMAKE-SCRIPTS %{buildroot}/usr/share/doc/kwin/cmake_modules_COPYING-CMAKE-SCRIPTS
pushd clr-build
%make_install
popd

%files
%defattr(-,root,root,-)
/usr/lib64/kconf_update_bin/kwin5_update_default_rules
/usr/lib64/libexec/kwin_killer_helper
/usr/lib64/libexec/kwin_rules_dialog
/usr/lib64/libexec/org_kde_kwin_xclipboard_syncer

%files bin
%defattr(-,root,root,-)
/usr/bin/kwin_wayland
/usr/bin/kwin_x11

%files data
%defattr(-,root,root,-)
/usr/share/config.kcfg/kwin.kcfg
/usr/share/config.kcfg/kwin_colorcorrect.kcfg
/usr/share/dbus-1/interfaces/org.kde.KWin.xml
/usr/share/dbus-1/interfaces/org.kde.kwin.ColorCorrect.xml
/usr/share/dbus-1/interfaces/org.kde.kwin.Compositing.xml
/usr/share/dbus-1/interfaces/org.kde.kwin.Effects.xml
/usr/share/icons/hicolor/16x16/apps/kwin.png
/usr/share/icons/hicolor/32x32/apps/kwin.png
/usr/share/icons/hicolor/48x48/apps/kwin.png
/usr/share/icons/hicolor/scalable/apps/kwin.svgz
/usr/share/knotifications5/kwin.notifyrc
/usr/share/kservices5/desktop.desktop
/usr/share/kservices5/kcmkwineffects.desktop
/usr/share/kservices5/kwin-script-desktopchangeosd.desktop
/usr/share/kservices5/kwin-script-enforcedeco.desktop
/usr/share/kservices5/kwin-script-minimizeall.desktop
/usr/share/kservices5/kwin-script-synchronizeskipswitcher.desktop
/usr/share/kservices5/kwin-script-videowall.desktop
/usr/share/kservices5/kwin/kwin4_decoration_qml_plastik.desktop
/usr/share/kservices5/kwin/kwin4_effect_dialogparent.desktop
/usr/share/kservices5/kwin/kwin4_effect_eyeonscreen.desktop
/usr/share/kservices5/kwin/kwin4_effect_fade.desktop
/usr/share/kservices5/kwin/kwin4_effect_fadedesktop.desktop
/usr/share/kservices5/kwin/kwin4_effect_frozenapp.desktop
/usr/share/kservices5/kwin/kwin4_effect_login.desktop
/usr/share/kservices5/kwin/kwin4_effect_logout.desktop
/usr/share/kservices5/kwin/kwin4_effect_maximize.desktop
/usr/share/kservices5/kwin/kwin4_effect_morphingpopups.desktop
/usr/share/kservices5/kwin/kwin4_effect_scalein.desktop
/usr/share/kservices5/kwin/kwin4_effect_translucency.desktop
/usr/share/kservices5/kwin/kwin4_effect_windowaperture.desktop
/usr/share/kservices5/kwinactions.desktop
/usr/share/kservices5/kwinadvanced.desktop
/usr/share/kservices5/kwincompositing.desktop
/usr/share/kservices5/kwindecoration.desktop
/usr/share/kservices5/kwinfocus.desktop
/usr/share/kservices5/kwinmoving.desktop
/usr/share/kservices5/kwinoptions.desktop
/usr/share/kservices5/kwinrules.desktop
/usr/share/kservices5/kwinscreenedges.desktop
/usr/share/kservices5/kwinscripts.desktop
/usr/share/kservices5/kwintabbox.desktop
/usr/share/kservices5/kwintouchscreen.desktop
/usr/share/kservicetypes5/kwindecoration.desktop
/usr/share/kservicetypes5/kwindesktopswitcher.desktop
/usr/share/kservicetypes5/kwineffect.desktop
/usr/share/kservicetypes5/kwinscript.desktop
/usr/share/kservicetypes5/kwinwindowswitcher.desktop
/usr/share/kwin/aurorae/AppMenuButton.qml
/usr/share/kwin/aurorae/AuroraeButton.qml
/usr/share/kwin/aurorae/AuroraeButtonGroup.qml
/usr/share/kwin/aurorae/AuroraeMaximizeButton.qml
/usr/share/kwin/aurorae/Decoration.qml
/usr/share/kwin/aurorae/DecorationButton.qml
/usr/share/kwin/aurorae/MenuButton.qml
/usr/share/kwin/aurorae/aurorae.qml
/usr/share/kwin/cubecap.png
/usr/share/kwin/decorations/kwin4_decoration_qml_plastik/contents/config/main.xml
/usr/share/kwin/decorations/kwin4_decoration_qml_plastik/contents/ui/PlastikButton.qml
/usr/share/kwin/decorations/kwin4_decoration_qml_plastik/contents/ui/config.ui
/usr/share/kwin/decorations/kwin4_decoration_qml_plastik/contents/ui/main.qml
/usr/share/kwin/decorations/kwin4_decoration_qml_plastik/metadata.desktop
/usr/share/kwin/effects/desktopgrid/main.qml
/usr/share/kwin/effects/kwin4_effect_dialogparent/contents/code/main.js
/usr/share/kwin/effects/kwin4_effect_dialogparent/metadata.desktop
/usr/share/kwin/effects/kwin4_effect_eyeonscreen/contents/code/main.js
/usr/share/kwin/effects/kwin4_effect_eyeonscreen/metadata.desktop
/usr/share/kwin/effects/kwin4_effect_fade/contents/code/main.js
/usr/share/kwin/effects/kwin4_effect_fade/contents/config/main.xml
/usr/share/kwin/effects/kwin4_effect_fade/metadata.desktop
/usr/share/kwin/effects/kwin4_effect_fadedesktop/contents/code/main.js
/usr/share/kwin/effects/kwin4_effect_fadedesktop/metadata.desktop
/usr/share/kwin/effects/kwin4_effect_frozenapp/contents/code/main.js
/usr/share/kwin/effects/kwin4_effect_frozenapp/metadata.desktop
/usr/share/kwin/effects/kwin4_effect_login/contents/code/main.js
/usr/share/kwin/effects/kwin4_effect_login/contents/config/main.xml
/usr/share/kwin/effects/kwin4_effect_login/contents/ui/config.ui
/usr/share/kwin/effects/kwin4_effect_login/metadata.desktop
/usr/share/kwin/effects/kwin4_effect_logout/contents/code/main.js
/usr/share/kwin/effects/kwin4_effect_logout/metadata.desktop
/usr/share/kwin/effects/kwin4_effect_maximize/contents/code/maximize.js
/usr/share/kwin/effects/kwin4_effect_maximize/metadata.desktop
/usr/share/kwin/effects/kwin4_effect_morphingpopups/contents/code/morphingpopups.js
/usr/share/kwin/effects/kwin4_effect_morphingpopups/metadata.desktop
/usr/share/kwin/effects/kwin4_effect_scalein/contents/code/main.js
/usr/share/kwin/effects/kwin4_effect_scalein/metadata.desktop
/usr/share/kwin/effects/kwin4_effect_translucency/contents/code/main.js
/usr/share/kwin/effects/kwin4_effect_translucency/contents/config/main.xml
/usr/share/kwin/effects/kwin4_effect_translucency/contents/ui/config.ui
/usr/share/kwin/effects/kwin4_effect_translucency/metadata.desktop
/usr/share/kwin/effects/kwin4_effect_windowaperture/contents/code/main.js
/usr/share/kwin/effects/kwin4_effect_windowaperture/metadata.desktop
/usr/share/kwin/effects/presentwindows/main.qml
/usr/share/kwin/kcm_kwindecoration/ButtonGroup.qml
/usr/share/kwin/kcm_kwindecoration/Buttons.qml
/usr/share/kwin/kcm_kwindecoration/Previews.qml
/usr/share/kwin/kcm_kwindecoration/main.qml
/usr/share/kwin/kcm_kwintabbox/dolphin.png
/usr/share/kwin/kcm_kwintabbox/kmail.png
/usr/share/kwin/kcm_kwintabbox/konqueror.png
/usr/share/kwin/kcm_kwintabbox/systemsettings.png
/usr/share/kwin/onscreennotification/plasma/dummydata/osd.qml
/usr/share/kwin/onscreennotification/plasma/main.qml
/usr/share/kwin/outline/plasma/outline.qml
/usr/share/kwin/scripts/desktopchangeosd/contents/ui/main.qml
/usr/share/kwin/scripts/desktopchangeosd/contents/ui/osd.qml
/usr/share/kwin/scripts/desktopchangeosd/metadata.desktop
/usr/share/kwin/scripts/enforcedeco/contents/code/main.js
/usr/share/kwin/scripts/enforcedeco/metadata.desktop
/usr/share/kwin/scripts/minimizeall/contents/code/main.js
/usr/share/kwin/scripts/minimizeall/metadata.desktop
/usr/share/kwin/scripts/synchronizeskipswitcher/contents/code/main.js
/usr/share/kwin/scripts/synchronizeskipswitcher/metadata.desktop
/usr/share/kwin/scripts/videowall/contents/code/main.js
/usr/share/kwin/scripts/videowall/contents/config/main.xml
/usr/share/kwin/scripts/videowall/contents/ui/config.ui
/usr/share/kwin/scripts/videowall/metadata.desktop
/usr/share/kwin/tm_inner.png
/usr/share/kwin/tm_outer.png
/usr/share/kwin/virtualkeyboard/main.qml
/usr/share/kwincompositing/qml/Effect.qml
/usr/share/kwincompositing/qml/EffectView.qml
/usr/share/kwincompositing/qml/Video.qml
/usr/share/kwincompositing/qml/main.qml

%files dev
%defattr(-,root,root,-)
/usr/include/kwin_export.h
/usr/include/kwinanimationeffect.h
/usr/include/kwinconfig.h
/usr/include/kwineffects.h
/usr/include/kwineffects_export.h
/usr/include/kwinglobals.h
/usr/include/kwinglplatform.h
/usr/include/kwingltexture.h
/usr/include/kwinglutils.h
/usr/include/kwinglutils_export.h
/usr/include/kwinglutils_funcs.h
/usr/include/kwinxrenderutils.h
/usr/include/kwinxrenderutils_export.h
/usr/lib64/cmake/KWinDBusInterface/KWinDBusInterfaceConfig.cmake
/usr/lib64/libkdeinit5_kwin_rules_dialog.so
/usr/lib64/libkdeinit5_kwin_x11.so
/usr/lib64/libkwin4_effect_builtins.so
/usr/lib64/libkwineffects.so
/usr/lib64/libkwinglutils.so
/usr/lib64/libkwinxrenderutils.so

%files doc
%defattr(0644,root,root,0755)
/usr/share/doc/HTML/en/kcontrol/desktop/index.cache.bz2
/usr/share/doc/HTML/en/kcontrol/desktop/index.docbook
/usr/share/doc/HTML/en/kcontrol/kwindecoration/button.png
/usr/share/doc/HTML/en/kcontrol/kwindecoration/configure.png
/usr/share/doc/HTML/en/kcontrol/kwindecoration/decoration.png
/usr/share/doc/HTML/en/kcontrol/kwindecoration/index.cache.bz2
/usr/share/doc/HTML/en/kcontrol/kwindecoration/index.docbook
/usr/share/doc/HTML/en/kcontrol/kwindecoration/main.png
/usr/share/doc/HTML/en/kcontrol/kwineffects/configure-effects.png
/usr/share/doc/HTML/en/kcontrol/kwineffects/configure-filter.png
/usr/share/doc/HTML/en/kcontrol/kwineffects/dialog-information.png
/usr/share/doc/HTML/en/kcontrol/kwineffects/index.cache.bz2
/usr/share/doc/HTML/en/kcontrol/kwineffects/index.docbook
/usr/share/doc/HTML/en/kcontrol/kwineffects/video.png
/usr/share/doc/HTML/en/kcontrol/kwinscreenedges/index.cache.bz2
/usr/share/doc/HTML/en/kcontrol/kwinscreenedges/index.docbook
/usr/share/doc/HTML/en/kcontrol/kwintabbox/index.cache.bz2
/usr/share/doc/HTML/en/kcontrol/kwintabbox/index.docbook
/usr/share/doc/HTML/en/kcontrol/windowbehaviour/index.cache.bz2
/usr/share/doc/HTML/en/kcontrol/windowbehaviour/index.docbook
/usr/share/doc/HTML/en/kcontrol/windowspecific/Face-smile.png
/usr/share/doc/HTML/en/kcontrol/windowspecific/akgregator-info.png
/usr/share/doc/HTML/en/kcontrol/windowspecific/akregator-attributes.png
/usr/share/doc/HTML/en/kcontrol/windowspecific/akregator-fav.png
/usr/share/doc/HTML/en/kcontrol/windowspecific/config-win-behavior.png
/usr/share/doc/HTML/en/kcontrol/windowspecific/emacs-attribute.png
/usr/share/doc/HTML/en/kcontrol/windowspecific/emacs-info.png
/usr/share/doc/HTML/en/kcontrol/windowspecific/focus-stealing-pop2top-attribute.png
/usr/share/doc/HTML/en/kcontrol/windowspecific/index.cache.bz2
/usr/share/doc/HTML/en/kcontrol/windowspecific/index.docbook
/usr/share/doc/HTML/en/kcontrol/windowspecific/knotes-attribute.png
/usr/share/doc/HTML/en/kcontrol/windowspecific/knotes-info.png
/usr/share/doc/HTML/en/kcontrol/windowspecific/kopete-attribute-2.png
/usr/share/doc/HTML/en/kcontrol/windowspecific/kopete-chat-attribute.png
/usr/share/doc/HTML/en/kcontrol/windowspecific/kopete-chat-info.png
/usr/share/doc/HTML/en/kcontrol/windowspecific/kopete-info.png
/usr/share/doc/HTML/en/kcontrol/windowspecific/kwin-detect-window.png
/usr/share/doc/HTML/en/kcontrol/windowspecific/kwin-kopete-rules.png
/usr/share/doc/HTML/en/kcontrol/windowspecific/kwin-rule-editor.png
/usr/share/doc/HTML/en/kcontrol/windowspecific/kwin-rules-main-n-akregator.png
/usr/share/doc/HTML/en/kcontrol/windowspecific/kwin-rules-main.png
/usr/share/doc/HTML/en/kcontrol/windowspecific/kwin-rules-ordering.png
/usr/share/doc/HTML/en/kcontrol/windowspecific/kwin-window-attributes.png
/usr/share/doc/HTML/en/kcontrol/windowspecific/kwin-window-matching.png
/usr/share/doc/HTML/en/kcontrol/windowspecific/pager-4-desktops.png
/usr/share/doc/HTML/en/kcontrol/windowspecific/tbird-compose-attribute.png
/usr/share/doc/HTML/en/kcontrol/windowspecific/tbird-compose-info.png
/usr/share/doc/HTML/en/kcontrol/windowspecific/tbird-main-attribute.png
/usr/share/doc/HTML/en/kcontrol/windowspecific/tbird-main-info.png
/usr/share/doc/HTML/en/kcontrol/windowspecific/tbird-reminder-attribute-2.png
/usr/share/doc/HTML/en/kcontrol/windowspecific/tbird-reminder-info.png
/usr/share/doc/HTML/en/kcontrol/windowspecific/window-matching-emacs.png
/usr/share/doc/HTML/en/kcontrol/windowspecific/window-matching-init.png
/usr/share/doc/HTML/en/kcontrol/windowspecific/window-matching-knotes.png
/usr/share/doc/HTML/en/kcontrol/windowspecific/window-matching-kopete-chat.png
/usr/share/doc/HTML/en/kcontrol/windowspecific/window-matching-kopete.png
/usr/share/doc/HTML/en/kcontrol/windowspecific/window-matching-ready-akregator.png
/usr/share/doc/HTML/en/kcontrol/windowspecific/window-matching-tbird-compose.png
/usr/share/doc/HTML/en/kcontrol/windowspecific/window-matching-tbird-main.png
/usr/share/doc/HTML/en/kcontrol/windowspecific/window-matching-tbird-reminder.png

%files lib
%defattr(-,root,root,-)
/usr/lib64/libkwin.so.5
/usr/lib64/libkwin.so.5.13.4
/usr/lib64/libkwin4_effect_builtins.so.1
/usr/lib64/libkwin4_effect_builtins.so.1.0.0
/usr/lib64/libkwineffects.so.11
/usr/lib64/libkwineffects.so.5.13.4
/usr/lib64/libkwinglutils.so.11
/usr/lib64/libkwinglutils.so.5.13.4
/usr/lib64/libkwinxrenderutils.so.11
/usr/lib64/libkwinxrenderutils.so.5.13.4
/usr/lib64/qt5/plugins/kcm_kwin_scripts.so
/usr/lib64/qt5/plugins/kcm_kwindecoration.so
/usr/lib64/qt5/plugins/kcm_kwindesktop.so
/usr/lib64/qt5/plugins/kcm_kwinoptions.so
/usr/lib64/qt5/plugins/kcm_kwinrules.so
/usr/lib64/qt5/plugins/kcm_kwinscreenedges.so
/usr/lib64/qt5/plugins/kcm_kwintabbox.so
/usr/lib64/qt5/plugins/kcm_kwintouchscreen.so
/usr/lib64/qt5/plugins/kf5/org.kde.kidletime.platforms/KF5IdleTimeKWinWaylandPrivatePlugin.so
/usr/lib64/qt5/plugins/kpackage/packagestructure/kwin_packagestructure_aurorae.so
/usr/lib64/qt5/plugins/kpackage/packagestructure/kwin_packagestructure_decoration.so
/usr/lib64/qt5/plugins/kpackage/packagestructure/kwin_packagestructure_scripts.so
/usr/lib64/qt5/plugins/kpackage/packagestructure/kwin_packagestructure_windowswitcher.so
/usr/lib64/qt5/plugins/kwin/effects/configs/kcm_kwin4_genericscripted.so
/usr/lib64/qt5/plugins/kwin/effects/configs/kwin_blur_config.so
/usr/lib64/qt5/plugins/kwin/effects/configs/kwin_coverswitch_config.so
/usr/lib64/qt5/plugins/kwin/effects/configs/kwin_cube_config.so
/usr/lib64/qt5/plugins/kwin/effects/configs/kwin_cubeslide_config.so
/usr/lib64/qt5/plugins/kwin/effects/configs/kwin_desktopgrid_config.so
/usr/lib64/qt5/plugins/kwin/effects/configs/kwin_diminactive_config.so
/usr/lib64/qt5/plugins/kwin/effects/configs/kwin_flipswitch_config.so
/usr/lib64/qt5/plugins/kwin/effects/configs/kwin_glide_config.so
/usr/lib64/qt5/plugins/kwin/effects/configs/kwin_invert_config.so
/usr/lib64/qt5/plugins/kwin/effects/configs/kwin_lookingglass_config.so
/usr/lib64/qt5/plugins/kwin/effects/configs/kwin_magiclamp_config.so
/usr/lib64/qt5/plugins/kwin/effects/configs/kwin_magnifier_config.so
/usr/lib64/qt5/plugins/kwin/effects/configs/kwin_mouseclick_config.so
/usr/lib64/qt5/plugins/kwin/effects/configs/kwin_mousemark_config.so
/usr/lib64/qt5/plugins/kwin/effects/configs/kwin_presentwindows_config.so
/usr/lib64/qt5/plugins/kwin/effects/configs/kwin_resize_config.so
/usr/lib64/qt5/plugins/kwin/effects/configs/kwin_showfps_config.so
/usr/lib64/qt5/plugins/kwin/effects/configs/kwin_slide_config.so
/usr/lib64/qt5/plugins/kwin/effects/configs/kwin_thumbnailaside_config.so
/usr/lib64/qt5/plugins/kwin/effects/configs/kwin_trackmouse_config.so
/usr/lib64/qt5/plugins/kwin/effects/configs/kwin_windowgeometry_config.so
/usr/lib64/qt5/plugins/kwin/effects/configs/kwin_wobblywindows_config.so
/usr/lib64/qt5/plugins/kwin/effects/configs/kwin_zoom_config.so
/usr/lib64/qt5/plugins/kwincompositing.so
/usr/lib64/qt5/plugins/org.kde.kdecoration2/kwin5_aurorae.so
/usr/lib64/qt5/plugins/org.kde.kglobalaccel5.platforms/KF5GlobalAccelPrivateKWin.so
/usr/lib64/qt5/plugins/org.kde.kwin.platforms/KWinX11Platform.so
/usr/lib64/qt5/plugins/org.kde.kwin.scenes/KWinSceneOpenGL.so
/usr/lib64/qt5/plugins/org.kde.kwin.scenes/KWinSceneQPainter.so
/usr/lib64/qt5/plugins/org.kde.kwin.scenes/KWinSceneXRender.so
/usr/lib64/qt5/plugins/org.kde.kwin.waylandbackends/KWinWaylandDrmBackend.so
/usr/lib64/qt5/plugins/org.kde.kwin.waylandbackends/KWinWaylandFbdevBackend.so
/usr/lib64/qt5/plugins/org.kde.kwin.waylandbackends/KWinWaylandVirtualBackend.so
/usr/lib64/qt5/plugins/org.kde.kwin.waylandbackends/KWinWaylandWaylandBackend.so
/usr/lib64/qt5/plugins/org.kde.kwin.waylandbackends/KWinWaylandX11Backend.so
/usr/lib64/qt5/plugins/platforms/KWinQpaPlugin.so
/usr/lib64/qt5/qml/org/kde/kwin/decoration/AppMenuButton.qml
/usr/lib64/qt5/qml/org/kde/kwin/decoration/ButtonGroup.qml
/usr/lib64/qt5/qml/org/kde/kwin/decoration/Decoration.qml
/usr/lib64/qt5/qml/org/kde/kwin/decoration/DecorationButton.qml
/usr/lib64/qt5/qml/org/kde/kwin/decoration/MenuButton.qml
/usr/lib64/qt5/qml/org/kde/kwin/decoration/libdecorationplugin.so
/usr/lib64/qt5/qml/org/kde/kwin/decoration/qmldir
/usr/lib64/qt5/qml/org/kde/kwin/decorations/plastik/libplastikplugin.so
/usr/lib64/qt5/qml/org/kde/kwin/decorations/plastik/qmldir
/usr/lib64/qt5/qml/org/kde/kwin/private/kdecoration/libkdecorationprivatedeclarative.so
/usr/lib64/qt5/qml/org/kde/kwin/private/kdecoration/qmldir

%files license
%defattr(-,root,root,-)
/usr/share/doc/kwin/COPYING
/usr/share/doc/kwin/COPYING.DOC
/usr/share/doc/kwin/cmake_modules_COPYING-CMAKE-SCRIPTS
