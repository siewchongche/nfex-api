def get_phrase(data):
    if 'b1' in data:
        data['买1价(buy 1 price)'] = data.pop('b1')
    if 'bvol' in data:
        data['24小时成交量, 按交易货币统计(24-hour trading volume, statistics by trading currency)'] = data.pop('bvol')
    if 'ch' in data:
        data['涨跌额(change amount) = (Last-Open24h)'] = data.pop('ch')
    if 'cp' in data:
        data['涨跌幅(quote change) = (Last-Open24h) / Last'] = data.pop('cp')
    if 'df' in data:
        data['盘口价差(handicap spread) = abs(Buy1-Sell1)'] = data.pop('df')
    if 'fp' in data:
        data['标记价格(mark price)'] = data.pop('fp')
    if 'fr' in data:
        data['资金费率(funding rate)'] = data.pop('fr')
    if 'ftm' in data:
        data['本期资金费率时间戳(timestamp of current funding rate)'] = data.pop('ftm')
    if 'hp' in data:
        data['24小时最高(24 hour maximum)'] = data.pop('hp')
    if 'hv' in data:
        data['总持仓量(total open interest)'] = data.pop('hv')
    if 'ip' in data:
        data['指数价格(index price)'] = data.pop('ip')
    if 'ip_twap' in data:
        data['指数价格(TWAP) Index Price (TWAP)'] = data.pop('ip_twap')
    if 'last' in data:
        data['最新成交价(latest transaction price)'] = data.pop('last')
    if 'lp' in data:
        data['24小时最低(24 hours minimum)'] = data.pop('lp')
    if 'lvol' in data:
        data['最新成交量(latest volume)'] = data.pop('lvol')
    if 'ncc_ts' in data:
        data['下次收取资金费用时间(the next time to charge funds)'] = data.pop('ncc_ts')
    if 'nfr' in data:
        data['预计资金费率(estimated funding rate)'] = data.pop('nfr')
    if 'nft_hv' in data:
        data['总持仓量标记价格(total open interest mark price)'] = data.pop('nft_hv')
    if 'nftm' in data:
        data['预计资金费率时间戳(estimated funding rate timestamp)'] = data.pop('nftm')
    if 'op' in data:
        data['开盘价(opening price)'] = data.pop('op')
    if 'pur' in data:
        data['多空人数比(long-short ratio)'] = data.pop('pur')
    if 's1' in data:
        data['卖1价(sell 1 price)'] = data.pop('s1')
    if 'sid' in data:
        data['交易对id(trade pair id)'] = data.pop('sid')
    if 'tm' in data:
        data['系统时间戳, 秒(system timestamp)'] = data.pop('tm')
    if 'vol' in data:
        data['订单量(order volume) / 24小时成交额, 按计价货币统计(24-hour turnover, calculated by pricing currency)'] = data.pop('vol')
    if 'custom_id' in data:
        data['客户端定义的ID标识(client-defined ID)'] = data.pop('custom_id')
    if 'done_amount' in data:
        data['成交量 (done amount)'] = data.pop('done_amount')
    if 'ava' in data:
        data['可用额(avaliable balance)'] = data.pop('ava')
    if 'balance' in data:
        data['余额(balance)'] = data.pop('balance')
    if 'ccy' in data:
        data['coin'] = data.pop('ccy')
    if 'change_type' in data:
        data['资产变化原因类型(change reseaon)'] = data.pop('change_type')
    if 'cro_un_pnl' in data:
        data['全仓未实现盈亏(full position unrealized profit and loss)'] = data.pop('cro_un_pnl')
    if 'freeze' in data:
        data['冻结额(freeze balance)'] = data.pop('freeze')
    if 'isol_frz' in data:
        data['逐仓冻结资产(freezing assets by margin)'] = data.pop('isol_frz')
    if 'isol_un_pnl' in data:
        data['逐仓未实现盈亏(isolated margin unrealized P&L)'] = data.pop('isol_un_pnl')
    if 'max_withdraw_amount' in data:
        data['最大可提取金额(maximum withdrawable amount)'] = data.pop('max_withdraw_amount')
    if 'simulation_balance' in data:
        data['模拟金额(simulation balance)'] = data.pop('simulation_balance')
    if 'total_im' in data:
        data['所有仓位保证金(margin for all positions)'] = data.pop('total_im')
    if 'uid' in data:
        data['用户ID(account id)'] = data.pop('uid')
    if 'un_pnl' in data:
        data['未实现盈亏(unrealized profit and loss)'] = data.pop('un_pnl')
    if 'wd_frz' in data:
        data['提现冻结资产(withdraw freeze assets)'] = data.pop('wd_frz')
    if 'count' in data:
        data['总条数(all count)'] = data.pop('count')
    if 'action' in data:
        data['动作(action)'] = data.pop('action')
    if 'bill_id' in data:
        data['账单id(bill id)'] = data.pop('bill_id')
    if 'change' in data:
        data['数额(amount)'] = data.pop('change')
    if 'close_price' in data:
        data['平仓价格 (liquidate_price)'] = data.pop('close_price')
    if 'close_vol' in data:
        data['平仓量 (close vol)'] = data.pop('close_vol')
    if 'coin' in data:
        data['币种(coin code)'] = data.pop('coin')
    if 'created_at' in data:
        data['创建时间(created time)'] = data.pop('created_at')
    if 'deal_price' in data:
        data['成交价 (deal price)'] = data.pop('deal_price')
    if 'deal_vol' in data:
        data['成交量 (deal vol)'] = data.pop('deal_vol')
    if 'fee_ratio' in data:
        data['手续费率 (fee rate)'] = data.pop('fee_ratio')
    if 'hold_vol' in data:
        data['持仓量 (open interest)'] = data.pop('hold_vol')
    if 'open_av' in data:
        data['开仓均价 (average opening price)'] = data.pop('open_av')
    if 'symbol_id' in data:
        data['交易对id (trade pair id)'] = data.pop('symbol_id')
    if 'symbol_name' in data:
        data['交易对名字 (trade pair name)'] = data.pop('symbol_name')
    if 'page_count' in data:
        data['总页数(page count)'] = data.pop('page_count')
    if 'page_num' in data:
        data['当前页(page num)'] = data.pop('page_num')
    if 'page_size' in data:
        data['每页条数(page size)'] = data.pop('page_size')
    if 'done_fee' in data:
        data['手续费 (transaction fees)'] = data.pop('done_fee')
    if 'done_vol' in data:
        data['成交量(done volume)'] = data.pop('done_vol')
    if 'finish_code' in data:
        data['结束码, 1 取消(cancel), 2 全部成交(full transaction), 3 部分成交(partial transaction), 4 失败(failure)'] = data.pop('finish_code')
    if 'maker_fee' in data:
        data['maker 手续费(maker fee)'] = data.pop('maker_fee')
    if 'o_mode' in data:
        data['1:普通订单(ordinary order) 2:强平订单(forced liquidation order) 3:破产订单(bankruptcy order) 4:减仓订单(lighten up order) 5:降档订单(downshift order), 7:止赢(take profit) 8:止损(stop loss)'] = data.pop('o_mode')
    if 'o_status' in data:
        data['订单状态(order status) Pending: 委托中 Finished: 完成'] = data.pop('o_status')
    if 'o_strategy' in data:
        data['订单策略(order strategy) {GTC:一直有效至取消(valid until canceled)}'] = data.pop('o_strategy')
    if 'o_type' in data:
        data['订单类型(order type) limit,market'] = data.pop('o_type')
    if 'o_way' in data:
        data['订单委托方向 1: 开多(open long) 2: 平空(close short) 3: 开空(open short) 4: 平多(close long)'] = data.pop('o_way')
    if 'order_id' in data:
        data['订单id(order id)'] = data.pop('order_id')
    if 'price' in data:
        data['价格(price)'] = data.pop('price')
    if 'tail_trigger_price' in data:
        data['条件单触发价格(conditional order trigger price)'] = data.pop('tail_trigger_price')
    if 'tail_trigger_type' in data:
        data['条件单触发价格类型(conditional order trigger price type)'] = data.pop('tail_trigger_type')
    if 'taker_fee' in data:
        data['taker 手续费(taker fee)'] = data.pop('taker_fee')
    if 'taker_av' in data:
        data['成交均价(average transaction price)'] = data.pop('taker_av')
    if 'available_leverage' in data:
        data['有效杠杆(effective leverage)'] = data.pop('available_leverage')
    if 'bankrupt_price' in data:
        data['破产价格(bankruptcy price)'] = data.pop('bankrupt_price')
    if 'close_fee' in data:
        data['预付的平仓手续费(prepaid closing fee)'] = data.pop('close_fee')
    if 'flag_price' in data:
        data['标记价格(flag price)'] = data.pop('flag_price')
    if 'frozen_vol' in data:
        data['冻结量(frozen volume)'] = data.pop('frozen_vol')
    if 'hold_av' in data:
        data['持仓均价(position avg price)'] = data.pop('hold_av')
    if 'im' in data:
        data['初始保证金(initial margin)'] = data.pop('im')
    if 'leverage' in data:
        data['初始杠杆，也就是仓位杠杆(leverage)'] = data.pop('leverage')
    if 'liquidate_price' in data:
        data['强平价格(liquidate_price)'] = data.pop('liquidate_price')
    if 'mm' in data:
        data['维持保证金(maintenance margin)'] = data.pop('mm')
    if 'original_im' in data:
        data['原始的起始保证金,不受资金费率的影响(origin initial margin)'] = data.pop('original_im')
    if 'realized_pnl' in data:
        data['已实现盈亏(realized profit and loss)'] = data.pop('realized_pnl')
    if 'roi' in data:
        data['收益率(rate of return)'] = data.pop('roi')
    if 'side' in data:
        data['仓位方向(position direction)'] = data.pop('side')
    if 'sl_price' in data:
        data['止损价格(stop loss price)'] = data.pop('sl_price')
    if 'sl_type' in data:
        data['止损价格类型(stop price type)'] = data.pop('sl_type')
    if 'status' in data:
        data['状态(status)'] = data.pop('status')
    if 'tp_price' in data:
        data['止赢价格(take profit price)'] = data.pop('tp_price')
    if 'tp_type' in data:
        data['止赢价格类型(take profit price type)'] = data.pop('tp_type')
    if 'type' in data:
        data['仓位类型(position type)'] = data.pop('type')
    if 'unrealized_pnl' in data:
        data['未实现盈亏(unrealized profit and loss)'] = data.pop('unrealized_pnl')
    if 'deal_price' in data:
        data['成交价 (deal price)'] = data.pop('deal_price')
    if 'deal_price' in data:
        data['成交价 (deal price)'] = data.pop('deal_price')
    

    return data

def get_phrases(data):
    if data:
        data = get_phrase(data)

        if type(data) == list:
            data_temp = []
            for each_data in data:
                data_with_phrase = get_phrase(each_data)
                data_temp.append(data_with_phrase)
            data = data_temp

        if 'data' in data:
            if type(data['data']) == list:
                data_temp = []
                for each_data in data['data']:
                    data_with_phrase = get_phrase(each_data)
                    data_temp.append(data_with_phrase)
                data['data'] = data_temp

    return data
