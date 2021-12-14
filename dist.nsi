; 该脚本使用 HM VNISEdit 脚本编辑器向导产生

; 安装程序初始定义常量
!define PRODUCT_NAME "水下发射高精度数值模拟软件"
!ifdef Version
    !define PRODUCT_VERSION "${Version}"
!else
    !define PRODUCT_VERSION "0.0.1"
!endif
!define PRODUCT_PUBLISHER "Romtek, Inc."
!define PRODUCT_WEB_SITE "http://www.romtek.cn"
!define PRODUCT_DIR_REGKEY "Software\Microsoft\Windows\CurrentVersion\App Paths\frog_ribon.exe"
!define PRODUCT_UNINST_KEY "Software\Microsoft\Windows\CurrentVersion\Uninstall\${PRODUCT_NAME}"
!define PRODUCT_UNINST_ROOT_KEY "HKLM"

SetCompressor lzma

; ------ MUI 现代界面定义 (1.67 版本以上兼容) ------
!include "MUI.nsh"

; MUI 预定义常量
!define MUI_ABORTWARNING
!define MUI_ICON "${NSISDIR}\Contrib\Graphics\Icons\classic-install.ico"
!define MUI_UNICON "${NSISDIR}\Contrib\Graphics\Icons\classic-uninstall.ico"

; 欢迎页面
!insertmacro MUI_PAGE_WELCOME
; 许可协议页面
!insertmacro MUI_PAGE_LICENSE "license.txt"
; 组件选择页面
!insertmacro MUI_PAGE_COMPONENTS
; 安装目录选择页面
!insertmacro MUI_PAGE_DIRECTORY
; 安装过程页面
!insertmacro MUI_PAGE_INSTFILES
; 安装完成页面
!define MUI_FINISHPAGE_RUN "$INSTDIR\frog_ribon.exe"
!insertmacro MUI_PAGE_FINISH

!define MUI_FINISHPAGE_SHOWREADME "$INSTDIR\release.txt"
!define MUI_FINISHPAGE_SHOWREADME_NOTCHECKED
!define MUI_FINISHPAGE_SHOWREADME_TEXT "查看更新说明"

; 安装卸载过程页面
!insertmacro MUI_UNPAGE_INSTFILES

; 安装界面包含的语言设置
!insertmacro MUI_LANGUAGE "SimpChinese"

; 安装预释放文件
!insertmacro MUI_RESERVEFILE_INSTALLOPTIONS
; ------ MUI 现代界面定义结束 ------

Name "${PRODUCT_NAME} ${PRODUCT_VERSION}"
OutFile "subns-V${PRODUCT_VERSION}-Setup64.exe"
InstallDir "$PROGRAMFILES\frog_ribon"
InstallDirRegKey HKLM "${PRODUCT_UNINST_KEY}" "UninstallString"
ShowInstDetails show
ShowUnInstDetails show

BrandingText "水下发射高精度数值模拟软件-V${PRODUCT_VERSION}"
BGGradient 000080 000080 ffffff
BGFont "宋体" 76 700 /ITALIC

Section "主程序" SEC01
  SectionIn 1 2 RO
  SetOutPath "$INSTDIR"
  SetOverwrite ifnewer
  File /r "dist\frog_ribon\*.*"
  CreateDirectory "$SMPROGRAMS\frog_ribon"
  CreateShortCut "$SMPROGRAMS\frog_ribon\subns ${PRODUCT_VERSION}.lnk" "$INSTDIR\frog_ribon.exe"
  CreateShortCut "$DESKTOP\subns ${PRODUCT_VERSION}.lnk" "$INSTDIR\frog_ribon.exe"
  File "dist\frog_ribon\frog_ribon.exe"
  File /r "3rd\*.*"
SectionEnd

Section /o "VC运行库" SEC02
  SectionIn 1
  SetOutPath "$INSTDIR"
  SetOverwrite ifnewer
  File "D:\temp\qt_env_3rd_extra\vcredist_2010_x64.exe"
  Exec "$INSTDIR\vcredist_2010_x64.exe"
SectionEnd

!insertmacro MUI_FUNCTION_DESCRIPTION_BEGIN
  !insertmacro MUI_DESCRIPTION_TEXT ${SEC01} "主程序"
  !insertmacro MUI_DESCRIPTION_TEXT ${SEC02} "VC运行环境"
!insertmacro MUI_FUNCTION_DESCRIPTION_END

Section -AdditionalIcons
  WriteIniStr "$INSTDIR\${PRODUCT_NAME}.url" "InternetShortcut" "URL" "${PRODUCT_WEB_SITE}"
  CreateShortCut "$SMPROGRAMS\frog_ribon\Website.lnk" "$INSTDIR\${PRODUCT_NAME}.url"
  CreateShortCut "$SMPROGRAMS\frog_ribon\Uninstall.lnk" "$INSTDIR\uninst.exe"
SectionEnd

Section -Post
  WriteUninstaller "$INSTDIR\uninst.exe"
  WriteRegStr HKLM "${PRODUCT_DIR_REGKEY}" "" "$INSTDIR\frog_ribon.exe"
  WriteRegStr ${PRODUCT_UNINST_ROOT_KEY} "${PRODUCT_UNINST_KEY}" "DisplayName" "$(^Name)"
  WriteRegStr ${PRODUCT_UNINST_ROOT_KEY} "${PRODUCT_UNINST_KEY}" "UninstallString" "$INSTDIR\uninst.exe"
  WriteRegStr ${PRODUCT_UNINST_ROOT_KEY} "${PRODUCT_UNINST_KEY}" "DisplayIcon" "$INSTDIR\frog_ribon.exe"
  WriteRegStr ${PRODUCT_UNINST_ROOT_KEY} "${PRODUCT_UNINST_KEY}" "DisplayVersion" "${PRODUCT_VERSION}"
  WriteRegStr ${PRODUCT_UNINST_ROOT_KEY} "${PRODUCT_UNINST_KEY}" "URLInfoAbout" "${PRODUCT_WEB_SITE}"
  WriteRegStr ${PRODUCT_UNINST_ROOT_KEY} "${PRODUCT_UNINST_KEY}" "Publisher" "${PRODUCT_PUBLISHER}"
SectionEnd

/******************************
 *  以下是安装程序的卸载部分  *
 ******************************/

Section Uninstall
  Delete "$INSTDIR\${PRODUCT_NAME}.url"
  Delete "$INSTDIR\uninst.exe"
  Delete "$INSTDIR\frog_ribon.exe"

  Delete "$SMPROGRAMS\frog_ribon\Uninstall.lnk"
  Delete "$SMPROGRAMS\frog_ribon\Website.lnk"
  Delete "$DESKTOP\水下发射高精度数值模拟软件.lnk"
  Delete "$SMPROGRAMS\frog_ribon\水下发射高精度数值模拟软件.lnk"

  RMDir "$SMPROGRAMS\frog_ribon"

  RMDir /r "$INSTDIR\wheel-0.36.2.dist-info"
  RMDir /r "$INSTDIR\tk"
  RMDir /r "$INSTDIR\tcl8"
  RMDir /r "$INSTDIR\tcl"
  RMDir /r "$INSTDIR\sqlalchemy"
  RMDir /r "$INSTDIR\setuptools-57.0.0.dist-info"
  RMDir /r "$INSTDIR\PyQt5"
  RMDir /r "$INSTDIR\pyinstaller-4.6.dist-info"
  RMDir /r "$INSTDIR\psycopg2"
  RMDir /r "$INSTDIR\PIL"
  RMDir /r "$INSTDIR\paginate_sqlalchemy"
  RMDir /r "$INSTDIR\paginate"
  RMDir /r "$INSTDIR\numpy"
  RMDir /r "$INSTDIR\matplotlib"
  RMDir /r "$INSTDIR\importlib_metadata-4.8.1.dist-info"
  RMDir /r "$INSTDIR\immutables"
  RMDir /r "$INSTDIR\greenlet"
  RMDir /r "$INSTDIR\altgraph-0.17.2.dist-info"

  RMDir "$INSTDIR"

  DeleteRegKey ${PRODUCT_UNINST_ROOT_KEY} "${PRODUCT_UNINST_KEY}"
  DeleteRegKey HKLM "${PRODUCT_DIR_REGKEY}"
  SetAutoClose true
SectionEnd

#-- 根据 NSIS 脚本编辑规则，所有 Function 区段必须放置在 Section 区段之后编写，以避免安装程序出现未可预知的问题。--#

Function .onInit
	System::Call 'kernel32::CreateMutexA(i 0, i 0, t "水下发射高精度数值模拟软件") i .r1 ?e'
	Pop $R0

	StrCmp $R0 0 +3
	 MessageBox MB_OK|MB_ICONEXCLAMATION "安装程序已经在运行！"
	 Abort
FunctionEnd

Function un.onInit
  MessageBox MB_ICONQUESTION|MB_YESNO|MB_DEFBUTTON2 "您确实要完全移除 $(^Name) ，及其所有的组件？" IDYES +2
  Abort
FunctionEnd

Function un.onUninstSuccess
  HideWindow
  MessageBox MB_ICONINFORMATION|MB_OK "$(^Name) 已成功地从您的计算机移除。"
FunctionEnd
