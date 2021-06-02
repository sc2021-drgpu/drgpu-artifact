HAS_SUBPARTITION_VALUES = 'q'
NO_SUBPARTITION_VALUES = 'n'

counters_name_map_for_ncu = {
    # warp_cant_issue
    "warp_cant_issue_barrier": ("smsp__average_warps_issue_stalled_barrier_per_issue_active.ratio", float),
    "warp_cant_issue_dispatch": ("smsp__average_warps_issue_stalled_dispatch_stall_per_issue_active.ratio", float),
    "warp_cant_issue_drain": ("smsp__average_warps_issue_stalled_drain_per_issue_active.ratio", float),
    "warp_cant_issue_imc_miss": ("smsp__average_warps_issue_stalled_imc_miss_per_issue_active.ratio", float),
    "warp_cant_issue_lg_throttle": ("smsp__average_warps_issue_stalled_lg_throttle_per_issue_active.ratio", float),
    "warp_cant_issue_long_scoreboard": (
        "smsp__average_warps_issue_stalled_long_scoreboard_per_issue_active.ratio", float),
    "warp_cant_issue_membar": ("smsp__average_warps_issue_stalled_membar_per_issue_active.ratio", float),
    "warp_cant_issue_mio_throttle": ("smsp__average_warps_issue_stalled_mio_throttle_per_issue_active.ratio", float),
    "warp_cant_issue_misc": ("smsp__average_warps_issue_stalled_misc_per_issue_active.ratio", float),
    "warp_cant_issue_no_inst": ("smsp__average_warps_issue_stalled_no_instruction_per_issue_active.ratio", float),
    "warp_cant_issue_pipe_throttle": (
        "smsp__average_warps_issue_stalled_math_pipe_throttle_per_issue_active.ratio", float),
    "warp_cant_issue_short_scoreboard": (
        "smsp__average_warps_issue_stalled_short_scoreboard_per_issue_active.ratio", float),
    "warp_cant_issue_wait": ("smsp__average_warps_issue_stalled_wait_per_issue_active.ratio", float),

    "issueIPC": ("sm__inst_issued.avg.per_cycle_active", float),

    # pipe
    "pipe_adu": ("sm__inst_executed_pipe_adu.avg.pct_of_peak_sustained_active", float),
    "pipe_alu": ("sm__inst_executed_pipe_alu.avg.pct_of_peak_sustained_active", float),
    "pipe_cbu": ("sm__inst_executed_pipe_cbu.avg.pct_of_peak_sustained_active", float),
    "pipe_fp16": ("sm__inst_executed_pipe_fp16.avg.pct_of_peak_sustained_active", float),
    "pipe_fp64": ("sm__inst_executed_pipe_fp64.avg.pct_of_peak_sustained_active", float),
    "pipe_ipa": ("sm__inst_executed_pipe_ipa.avg.pct_of_peak_sustained_active", float),
    "pipe_lsu": ("sm__inst_executed_pipe_lsu.avg.pct_of_peak_sustained_active", float),
    "pipe_tex": ("sm__inst_executed_pipe_tex.avg.pct_of_peak_sustained_active", float),
    "pipe_uniform": ("sm__inst_executed_pipe_uniform.avg.pct_of_peak_sustained_active", float),
    "pipe_xu": ("sm__inst_executed_pipe_xu.avg.pct_of_peak_sustained_active", float),
    "pipe_tensor_fp": ("sm__inst_executed_pipe_tensor_op_hmma.avg.pct_of_peak_sustained_active", float),
    "pipe_tensor_int": ("sm__inst_executed_pipe_tensor_op_imma.avg.pct_of_peak_sustained_active", float),
    "elapsedClocks": ("gpc__cycles_elapsed.max", float),
    # instruction distribution
    "inst_executed_op_bit": ("sm__sass_thread_inst_executed_op_bit_pred_on.sum", float),
    "inst_executed_op_control": ("sm__sass_thread_inst_executed_op_control_pred_on.sum", float),
    "inst_executed_op_conversion": ("sm__sass_thread_inst_executed_op_conversion_pred_on.sum", float),
    "inst_executed_op_fp16": ("sm__sass_thread_inst_executed_op_fp16_pred_on.sum", float),
    "inst_executed_op_fp32": ("sm__sass_thread_inst_executed_op_fp32_pred_on.sum", float),
    "inst_executed_op_fp64": ("sm__sass_thread_inst_executed_op_fp64_pred_on.sum", float),
    "inst_executed_op_integer": ("sm__sass_thread_inst_executed_op_integer_pred_on.sum", float),
    "inst_executed_op_inter_thread_communication": (
        "sm__sass_thread_inst_executed_op_inter_thread_communication_pred_on.sum", float),
    "inst_executed_op_memory": ("sm__sass_thread_inst_executed_op_memory_pred_on.sum", float),
    "inst_executed_op_misc": ("sm__sass_thread_inst_executed_op_misc_pred_on.sum", float),
    "inst_executed_op_uniform": ("sm__sass_thread_inst_executed_op_uniform_pred_on.sum", float),
    # @todo remove all float type, just use float as default type
    # make sure the prefix is different for different counter sets.
    "inst_mem_32b": ("sm__sass_inst_executed_op_memory_32b.sum", float),
    "inst_mem_64b": ("sm__sass_inst_executed_op_memory_64b.sum", float),
    "inst_mem_128b": ("sm__sass_inst_executed_op_memory_128b.sum", float),
    "inst_mem_gld_32b": ("", float),
    "inst_mem_gld_64b": ("", float),
    "inst_mem_gld_128b": ("", float),
    "inst_mem_geld_32b": ("", float),
    "inst_mem_geld_64b": ("", float),
    "inst_mem_geld_128b": ("", float),
    "inst_mem_ldgsts_32b": ("", float),
    "inst_mem_ldgsts_64b": ("", float),
    "inst_mem_ldgsts_128b": ("", float),
    "inst_mem_shared_ld_32b": ("", float),
    "inst_mem_shared_ld_64b": ("", float),
    "inst_mem_shared_ld_128b": ("", float),
    "inst_mem_shared_st_32b": ("", float),
    "inst_mem_shared_st_64b": ("", float),
    "inst_mem_shared_st_128b": ("", float),

    "gnic_lg_read_requests_postcoalescing": ("", float),
    "gnic_lg_read_requests_precoalescing": ("", float),
    # need to devided by 100
    "l1tex_hit_rate": ("l1tex__t_sector_hit_rate.pct", float),
    "l2_hit_rate": ("lts__t_sector_hit_rate.pct", float),

    "gnic_latency": ("", float),
    "mmu_ack_latency": ("", float),
    "generic_ld_latency": ("", float),
    "shmem_ld_latency": ("", float),
    "lg_ld_latency": ("", float),

    "ltp_utlb_hit": ("", float),
    "ltp_utlb_miss": ("", float),
    "l1_lines_per_instruction_avg": ("", float),
    "l1tex__t_set_accesses": ("l1tex__t_set_accesses.sum", float),
    "l1tex__t_requests": ("l1tex__t_requests.sum", float),
    'gpcl1_tlb_hit': ("", float),
    'gpcl1_tlb_miss': ("", float),
    "gnic_read_sectors_postcoalescing": ("l1tex__m_xbar2l1tex_read_sectors.sum", float),
    "fb_total_bytes": ("dram__bytes_read.sum", float),
    "global_ld_set_conflicts": ("l1tex__t_set_conflicts_pipe_lsu_mem_global_op_ld.sum", float),
    "global_ld_set_accesses": ("l1tex__t_set_accesses_pipe_lsu_mem_global_op_ld.sum", float),
    "ltp_utlb_arb_not_stalled": ("", float),
    "l2_bank_conflict": ("", float),
    "l2_data_bank_accesses": ("", float),
    "l2_requests": ("lts__t_requests.sum", float),
    "fb_accesses_per_activate": ("", float),
    "dram_util": ("", float),
    "dram_throughput": ("", float),
    "average_latency_reads": ("", float),
    "average_latency_writes": ("", float),
    "average_dram_banks": ("", float),
    "dram_lowBanks": ("", float),
    "dram_noReq": ("", float),
    "dram_turns": ("", float),
    "launch_block_size": ("launch__block_size", float),
    "imc_hitrate": ("", float),
    "activewarps_per_activecycle": ("sm__warps_active.avg.per_cycle_active", float),
    "shared_ld_data_conflicts": ("l1tex__data_bank_conflicts_pipe_lsu_mem_shared_op_ld.sum", float),
    "shared_ld_requests": ("", float),
    "shared_st_data_conflicts": ("l1tex__data_bank_conflicts_pipe_lsu_mem_shared_op_st.sum", float),
    "shared_st_requests": ("", float),
    "retireIPC": ("sm__inst_executed.avg.per_cycle_active", float),
    # for branch_solving_and_barrier_common, provided by 2020.3.0+
    "not_predicated_off_thread_per_inst_executed": (
        "sm__average_thread_inst_executed_pred_on_per_inst_executed_realtime.ratio", float),
    "not_predicated_off_thread_per_inst_executed2":("smsp__thread_inst_executed_pred_on_per_inst_executed.ratio", float),
    # SOLs
    "sol_sm": ("sm__throughput.avg.pct_of_peak_sustained_elapsed", float),
    "sol_l1": ("l1tex__throughput.avg.pct_of_peak_sustained_active", float),
    "sol_l2": ("lts__throughput.avg.pct_of_peak_sustained_elapsed", float),
    "sol_dram": ("dram__throughput.avg.pct_of_peak_sustained_elapsed", float),
    "sol_compute_memory": ("gpu__compute_memory_throughput.avg.pct_of_peak_sustained_elapsed", float),
    "theoretical_active_warps": ("sm__maximum_warps_avg_per_active_cycle", float),
    "block_limit_sm": ("launch__occupancy_limit_blocks", float),
    "block_limit_shared_mem": ("launch__occupancy_limit_shared_mem", float),
    "block_limit_register": ("launch__occupancy_limit_registers", float),
    "block_limit_warps": ("launch__occupancy_limit_warps", float),
    "register_per_thread": ("launch__registers_per_thread", int),
}
