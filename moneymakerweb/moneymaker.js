import { app } from "../../scripts/app.js";
import { ComfyWidgets } from "../../scripts/widgets.js";

app.registerExtension({
    name: "MoneyMaker.ShowNodes",
    async beforeRegisterNodeDef(nodeType, nodeData) {
        // 处理 SomethingShow 节点
        if (nodeData.name === "SomethingShow") {
            // 在节点初始化时创建控件
            nodeType.prototype.onNodeCreated = function() {
                this.dynamicInputWidget = ComfyWidgets["STRING"](this, "dynamic_input", ["STRING", { multiline: true }], app).widget;
                this.dynamicInputWidget.inputEl.readOnly = true; // 设置为只读
                this.dynamicInputWidget.inputEl.style.opacity = 1.0; // 设置不透明度
            };

            const origOnExecuted = nodeType.prototype.onExecuted;
            
            nodeType.prototype.onExecuted = function(message) {
                origOnExecuted?.apply(this, arguments); // 保留原始逻辑
                
                // 更新已有控件的值
                if (this.dynamicInputWidget) {
                    this.dynamicInputWidget.value = message?.text || "";
                }
            };
        }

        // 处理 TensorShow 节点
        if (nodeData.name === "TensorShow") {
            // 在节点初始化时创建控件
            nodeType.prototype.onNodeCreated = function() {
                this.dynamicInputWidget = ComfyWidgets["STRING"](this, "dynamic_input", ["STRING", { multiline: true }], app).widget;
                this.dynamicInputWidget.inputEl.readOnly = true; // 设置为只读
                this.dynamicInputWidget.inputEl.style.opacity = 1.0; // 设置不透明度
                this.dynamicInputWidget.inputEl.style.fontFamily = "monospace";
                this.dynamicInputWidget.inputEl.style.whiteSpace = "pre-wrap";  // 保留换行符
            };

            const origOnExecuted = nodeType.prototype.onExecuted;
            
            nodeType.prototype.onExecuted = function(message) {
                origOnExecuted?.apply(this, arguments);
                
                // 更新已有控件的值
                if (this.dynamicInputWidget) {
                    this.dynamicInputWidget.value = message?.text || "";
                }
            };
        }
    }
});