#include "../node_shader_util.h"

//in nodes/shaders/nodes

static bNodeSocketTemplate sh_node_color_add_in[] = {
	{	SOCK_SHADER, 1, N_("Color")},
	{	SOCK_SHADER, 1, N_("Color")},
	{	-1, 0, ""	}
};

static bNodeSocketTemplate sh_node_color_add_out[] = {
	{	SOCK_SHADER, 0, N_("Color")},
	{	-1, 0, ""	}
};

static int node_shader_gpu_color_add(GPUMaterial *mat, bNode *node, bNodeExecData *UNUSED(execdata), GPUNodeStack *in, GPUNodeStack *out)
{
	return GPU_stack_link(mat, node, "node_color_add", in, out);
}

/* node type definition */
void register_node_type_sh_color_add(void)
{
	static bNodeType ntype;

	sh_node_type_base(&ntype, SH_NODE_ADD_SHADER, "Add Color", NODE_CLASS_SHADER, 0);
	node_type_socket_templates(&ntype, sh_node_color_add_in, sh_node_color_add_out);
	node_type_init(&ntype, NULL);
	node_type_storage(&ntype, "", NULL, NULL);
	node_type_gpu(&ntype, node_shader_gpu_color_add);

	nodeRegisterType(&ntype);
}
