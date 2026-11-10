# tools/

这个目录用来放第三方程序 **PinyinLexTool.exe**（约 69 MB），它**不随仓库提交**。

## 为什么要自己下载

`PinyinLexTool` 是别人用 MIT 许可证发布的开源工具，本仓库直接在 Release 的整合包里
附带它（并遵守 MIT 的声明要求），但 Git 仓库本身不存二进制，避免仓库膨胀。

## 怎么放

1. 打开 <https://github.com/mchudie/PinyinLexTool/releases>
2. 下载 `v1.0.1` 的 `PinyinLexTool.exe`
3. 放进本目录，路径应为 `tools\PinyinLexTool.exe`
4. 回到仓库根目录双击 `1-一键导入.bat`

## 校验

```powershell
Get-FileHash .\tools\PinyinLexTool.exe -Algorithm SHA256
```

本项目验证过的 v1.0.1：

```
EF08110086F2FF53FFBDBAE4D8965594349A6BA9604CC8C1EE7BABFFD895EFFA
```
