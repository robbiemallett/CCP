import numpy as np
import constants
def calculate_leading_edge_widths(waveforms):

    leading_edge_widths = np.empty(waveforms.shape[0])

    for i in np.arange(waveforms.shape[0]):
        waveform = np.array(waveforms[i])
        bin_70 = np.argmax(waveform > 7 * np.max(waveform) / 10)
        bin_30 = np.argmax(waveform > 3 * np.max(waveform) / 10)
        leading_edge_widths[i] = bin_70 - bin_30

    return(leading_edge_widths)

def classify_leads_floes(stack_peakiness_array, stack_standard_dev, leading_edge_widths):

    specular_echoes = np.where((stack_standard_dev < 6.28) & (stack_peakiness_array > 18), 1, 0)

    diffuse_echoes = np.where((stack_standard_dev > 6.28) & (stack_peakiness_array < 9), 1, 0)

    simple_leading_edges = np.where(leading_edge_widths <= 3, 1, 0)

    leads = np.multiply(specular_echoes, simple_leading_edges)
    floes = np.multiply(diffuse_echoes, simple_leading_edges)

    return(leads, floes)

def retrack_floes(waveforms, floes_mask, window_delays, threshold=50):

    floe_two_way_return_times = np.full(waveforms.shape[0], np.nan)

    for i in np.arange(waveforms.shape[0]):

        if floes_mask[i]:

            bin_threshold = np.argmax(waveforms[i] > threshold * np.max(waveforms[i]) / 100)

            time_before_128 = (128 - bin_threshold) * constants.bin_time

            floe_two_way_return_times[i] = window_delays[i] - time_before_128

    floe_two_way_return_times[floe_two_way_return_times > 1e270] = np.nan

    return(floe_two_way_return_times)

def retrack_leads(waveforms, leads_mask, window_delays):

    threshold = 99

    lead_two_way_return_times = np.full(waveforms.shape[0], np.nan)

    for i in np.arange(waveforms.shape[0]):

        if leads_mask[i]:

            bin_threshold = np.argmax(waveforms[i] > threshold * np.max(waveforms[i]) / 100)

            time_before_128 = (128 - bin_threshold) * bin_time

            lead_two_way_return_times[i] = window_delays[i] - time_before_128

    lead_two_way_return_times[lead_two_way_return_times > 1e270] = np.nan

    return(lead_two_way_return_times)

def interpolate_leads(lead_two_way_return_times):

    leads_copy = lead_two_way_return_times.copy()

    nan_args = np.argwhere(np.isnan(lead_two_way_return_times))[:, 0]

    good_args = np.argwhere(~np.isnan(lead_two_way_return_times))[:, 0]

    good_vals = lead_two_way_return_times[~np.isnan(lead_two_way_return_times)]

    leads_copy[np.isnan(leads_copy)] = np.interp(x=nan_args, xp=good_args, fp=good_vals)

    return(leads_copy)

def calculate_radar_freeboards(floe_two_way_return_times, interpolated_leads, mask_threshold = -2):

    radar_freeboards_time = (floe_two_way_return_times - interpolated_leads) / 2

    radar_freeboards_dist = radar_freeboards_time * constants.speed_of_light

    radar_freeboards_dist[radar_freeboards_dist < mask_threshold] = np.nan

    return(radar_freeboards_dist)