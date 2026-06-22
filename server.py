from fastmcp import FastMCP
from prefab_ui.app import PrefabApp
from prefab_ui.components import (
    Column, 
    Row, 
    Text, 
    Select, 
    SelectOption, 
    Switch, 
    If, 
    Metric
)
from prefab_ui.components.charts import BarChart, PieChart, LineChart, ChartSeries
from prefab_ui.rx import Rx

# Initialize the server under a completely generic identity
mcp = FastMCP("Universal Multi-Chart Visualizer")

@mcp.tool(app=True)
async def render_dynamic_dashboard(
    title: str,
    x_axis_labels: list[str],
    y_axis_values: list[int],
    metric_label: str = "Value",
    target_goal_value: str = None
) -> PrefabApp:
    """
    Renders an adaptive dashboard with dynamic item filtering AND chart type switches (Bar/Pie/Line).
    """
    
    # 1. Package the master dataset using completely generic keys
    all_data = [
        {"x_metric": str(x), "y_metric": int(y)} 
        for x, y in zip(x_axis_labels, y_axis_values)
    ]

    # 2. Add 'chart_type' into the starting state configuration
    state_payload = {
        "filter_view": "all",
        "chart_type": "bar", # Default visualization mode
        "show_target": True if target_goal_value else False,
        "data_all": all_data,
    }

    # Map individual segments for granular control filtering
    for x_item, y_val in zip(x_axis_labels, y_axis_values):
        clean_key = str(x_item).lower().strip().replace(" ", "_").replace("-", "_")
        state_payload[f"data_{clean_key}"] = [{"x_metric": str(x_item), "y_metric": int(y_val)}]

    # Assemble safe layout strings
    ternary_accumulator = "data_all"
    for x_item in x_axis_labels:
        clean_key = str(x_item).lower().strip().replace(" ", "_").replace("-", "_")
        ternary_accumulator = f"filter_view == '{clean_key}' ? data_{clean_key} : ({ternary_accumulator})"
        
    compiler_expression = f"{{{{ {ternary_accumulator} }}}}"

    # 3. Construct the application framework
    with PrefabApp(state=state_payload) as app:
        
        with Column(
            gap=4,
            css_class="p-6",
            let={"active_chart_dataset": compiler_expression},
        ):
            
            # CONTROL TOP-BAR
            with Row(gap=4, align="center", css_class="w-full justify-between items-center mb-2"):
                
                # LEFT: Item Filter Dropdown
                with Select(name="filter_view", css_class="w-52"):
                    SelectOption(value="all", label=f"All {metric_label} Items")
                    for x_item in x_axis_labels:
                        clean_key = str(x_item).lower().strip().replace(" ", "_").replace("-", "_")
                        SelectOption(value=clean_key, label=f"Only {x_item}")
                
                # RIGHT: Chart Engine Selector + Goal switches
                with Row(gap=3, align="center", css_class="ml-auto"):
                    
                    with Select(name="chart_type", css_class="w-36"):
                        SelectOption(value="bar", label="Bar Chart")
                        SelectOption(value="pie", label="Pie Chart")
                        SelectOption(value="line", label="Line Chart")
                    
                    if target_goal_value:
                        Text("|", css_class="text-muted-foreground/30 mx-1")
                        Switch(name="show_target", css_class="scale-90")
                        Text("Target Meter", css_class="text-xs font-medium text-muted-foreground")
            
            # 4. FIXED CHAMELEON CANVAS: Uses correct props depending on chart architecture
            with If(Rx("chart_type == 'bar'")):
                BarChart(
                    data=Rx("active_chart_dataset"),
                    series=[ChartSeries(data_key="y_metric", label=metric_label)],
                    x_axis="x_metric",
                )
            
            with If(Rx("chart_type == 'pie'")):
                # 💡 FIX: Removed series/x_axis and added data_key/name_key to satisfy schema validation
                PieChart(
                    data=Rx("active_chart_dataset"),
                    data_key="y_metric",
                    name_key="x_metric",
                    show_legend=True
                )
                
            with If(Rx("chart_type == 'line'")):
                LineChart(
                    data=Rx("active_chart_dataset"),
                    series=[ChartSeries(data_key="y_metric", label=metric_label)],
                    x_axis="x_metric",
                )
            
            # TARGET BOUNDARY PANEL
            if target_goal_value:
                with If(Rx("show_target")):
                    with Row(gap=4, css_class="mt-2"):
                        Metric(label=f"Target {metric_label} Goal", value=str(target_goal_value))

    return app

if __name__ == "__main__":
    mcp.run()